from typing import List

from solitaire.game import GOAL_STATE, SolitaireBoard
from solitaire.search import depth_first_search, Node


class TestNode:
    def test_relationship_correctly_set(self):
        root = Node(SolitaireBoard())
        child = Node(SolitaireBoard())

        root.add(child)

        assert child.parent == root
        assert len(root.children) == 1

    def test_depth(self):
        root = Node(SolitaireBoard())
        assert root.depth == 0

        # Build a tree by adding a new layer with each iteration of the loop
        previous = root
        for layer in range(1, 11):
            child = Node(SolitaireBoard())
            previous.add(child)
            assert child.depth == layer
            previous = child

        # Build another tree with a single wide layer
        root.children = []
        for _ in range(10):
            child = Node(SolitaireBoard())
            root.add(child)
            assert child.depth == 1

    def test_backtrace_from_root_returns_empty_list(self):
        root = Node(SolitaireBoard())
        assert root.backtrace() == []

    def test_backtrace_walks_back_correctly(self):
        root = Node(SolitaireBoard())

        created_children: List[Node] = []
        previous = root
        for _ in range(10):
            child = Node(SolitaireBoard())
            previous.add(child)
            previous = child
            created_children.append(child)

        created_children.reverse()
        assert previous.backtrace() == created_children


class TestDepthFirstSearch:
    def test_search_finds_goal_state_at_root(self):
        root = Node(SolitaireBoard(GOAL_STATE))

        assert depth_first_search(root) == root
