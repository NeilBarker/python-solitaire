import time

from solitaire.game import SolitaireBoard
from solitaire.search import depth_first_search, Node

if __name__ == "__main__":
    start_time = time.time()

    tree = Node(SolitaireBoard())
    goal_node = depth_first_search(tree)

    print(f"Found solution in {time.time() - start_time} seconds")
    print(f"at depth: {goal_node.depth}")

    for node in goal_node.backtrace():
        if node.from_move:
            print(f"{node.from_move.direction} from {node.from_move.origin}")
            for row in node.board.state:
                print(row)
            print()
        else:
            print("Something went wrong...")
