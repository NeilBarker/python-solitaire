from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Set

from solitaire.game import GOAL_STATE_STR, Move, SolitaireBoard


@dataclass
class Node:
    board: SolitaireBoard
    from_move: Optional[Move] = None
    parent: Optional[Node] = None

    children: List[Node] = field(default_factory=list, init=False)

    @property
    def depth(self) -> int:
        if self.parent:
            return 1 + self.parent.depth
        return 0

    def add(self, child: Node) -> None:
        child.parent = self
        self.children.append(child)

    def backtrace(self) -> List[Node]:
        if not self.parent:
            return []
        path: List[Node] = [self]
        path.extend(self.parent.backtrace())
        return path


def depth_first_search(tree: Node) -> Node:
    visited_nodes: Set[str] = set()
    frontier: List[Node] = [tree]

    while frontier:
        node = frontier.pop()

        state_str = node.board.state_str
        if state_str not in visited_nodes:
            if state_str == GOAL_STATE_STR:
                return node

            visited_nodes.add(state_str)
            for successor, move in node.board.successors():
                successor_node = Node(successor, move)
                node.add(successor_node)
                frontier.append(successor_node)

    raise RuntimeError("No solution found")
