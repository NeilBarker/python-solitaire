from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Generator, List, Tuple


BoardState = List[List[str]]
"""A 9x9 grid representing the solitaire board."""


GOAL_STATE: BoardState = [
    ["2", "2", "0", "0", "0", "2", "2"],
    ["2", "2", "0", "0", "0", "2", "2"],
    ["0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0"],
    ["2", "2", "0", "0", "0", "2", "2"],
    ["2", "2", "0", "0", "0", "2", "2"],
]
GOAL_STATE_STR = "".join("".join(row) for row in GOAL_STATE)


def make_initial_state() -> BoardState:
    return [
        ["2", "2", "1", "1", "1", "2", "2"],
        ["2", "2", "1", "1", "1", "2", "2"],
        ["1", "1", "1", "1", "1", "1", "1"],
        ["1", "1", "1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1", "1", "1"],
        ["2", "2", "1", "1", "1", "2", "2"],
        ["2", "2", "1", "1", "1", "2", "2"],
    ]


@dataclass
class BoardCoordinate:
    x: int
    y: int


class MoveDirection(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


@dataclass
class Move:
    direction: MoveDirection
    origin: BoardCoordinate


@dataclass
class SolitaireBoard:
    """Model of a solitaire board.

    This is a value type, any mutations return a new instance.

    """

    state: BoardState = field(default_factory=make_initial_state)

    @property
    def state_str(self) -> str:
        """Return a string describing the state of the board.

        This can be used as a hash value for the board.

        """
        return "".join("".join(row) for row in self.state)

    def possible_moves(self) -> Generator[Move, None, None]:
        for y in range(0, 7):
            for x in range(0, 7):
                if self.state[y][x] == "1":
                    if y >= 2:
                        if self.state[y - 1][x] == "1" and self.state[y - 2][x] == "0":
                            yield Move(MoveDirection.UP, BoardCoordinate(x, y))
                    if y <= 4:
                        if self.state[y + 1][x] == "1" and self.state[y + 2][x] == "0":
                            yield Move(MoveDirection.DOWN, BoardCoordinate(x, y))
                    if x >= 2:
                        if self.state[y][x - 1] == "1" and self.state[y][x - 2] == "0":
                            yield Move(MoveDirection.LEFT, BoardCoordinate(x, y))
                    if x <= 4:
                        if self.state[y][x + 1] == "1" and self.state[y][x + 2] == "0":
                            yield Move(MoveDirection.RIGHT, BoardCoordinate(x, y))

    def apply_move(self, move: Move) -> SolitaireBoard:
        new_state: BoardState = [row[:] for row in self.state]  # Fast copy
        if move.direction == MoveDirection.UP:
            new_state[move.origin.y][move.origin.x] = "0"
            new_state[move.origin.y - 1][move.origin.x] = "0"
            new_state[move.origin.y - 2][move.origin.x] = "1"
        elif move.direction == MoveDirection.DOWN:
            new_state[move.origin.y][move.origin.x] = "0"
            new_state[move.origin.y + 1][move.origin.x] = "0"
            new_state[move.origin.y + 2][move.origin.x] = "1"
        elif move.direction == MoveDirection.LEFT:
            new_state[move.origin.y][move.origin.x] = "0"
            new_state[move.origin.y][move.origin.x - 1] = "0"
            new_state[move.origin.y][move.origin.x - 2] = "1"
        else:
            new_state[move.origin.y][move.origin.x] = "0"
            new_state[move.origin.y][move.origin.x + 1] = "0"
            new_state[move.origin.y][move.origin.x + 2] = "1"
        return SolitaireBoard(new_state)

    def successors(self) -> Generator[Tuple[SolitaireBoard, Move], None, None]:
        for move in self.possible_moves():
            yield self.apply_move(move), move
