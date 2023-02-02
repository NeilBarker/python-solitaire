from solitaire.game import (
    GOAL_STATE,
    BoardCoordinate,
    Move,
    MoveDirection,
    SolitaireBoard,
)


class TestIdentifyMoves:
    def test_identifies_four_moves_from_initial_state(self):
        board = SolitaireBoard()
        moves = list(board.possible_moves())
        assert len(moves) == 4

        # Check the actual moves
        expected_moves = [
            Move(MoveDirection.UP, BoardCoordinate(3, 5)),
            Move(MoveDirection.DOWN, BoardCoordinate(3, 1)),
            Move(MoveDirection.LEFT, BoardCoordinate(5, 3)),
            Move(MoveDirection.RIGHT, BoardCoordinate(1, 3)),
        ]
        for actual_move in moves:
            assert actual_move in expected_moves

    def test_identifies_no_moves_from_goal_state(self):
        board = SolitaireBoard(GOAL_STATE)
        moves = list(board.possible_moves())
        assert len(moves) == 0

    def test_identifies_two_available_vertical_moves(self):
        state = [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "0", "0", "0", "2", "2", "2"],
            ["2", "2", "2", "0", "0", "0", "2", "2", "2"],
            ["2", "0", "0", "0", "1", "0", "0", "0", "2"],
            ["2", "0", "0", "0", "1", "0", "0", "0", "2"],
            ["2", "0", "0", "0", "1", "0", "0", "0", "2"],
            ["2", "2", "2", "0", "0", "0", "2", "2", "2"],
            ["2", "2", "2", "0", "0", "0", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2", "2", "2", "2"],
        ]
        board = SolitaireBoard(state)
        moves = list(board.possible_moves())
        assert len(moves) == 2

        expected_moves = [
            Move(MoveDirection.UP, BoardCoordinate(4, 4)),
            Move(MoveDirection.DOWN, BoardCoordinate(4, 4)),
        ]
        for actual_move in moves:
            assert actual_move in expected_moves

    def test_identifies_two_available_horizontal_moves(self):
        state = [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "0", "0", "0", "2", "2", "2"],
            ["2", "2", "2", "0", "0", "0", "2", "2", "2"],
            ["2", "0", "0", "0", "0", "0", "0", "0", "2"],
            ["2", "0", "0", "1", "1", "1", "0", "0", "2"],
            ["2", "0", "0", "0", "0", "0", "0", "0", "2"],
            ["2", "2", "2", "0", "0", "0", "2", "2", "2"],
            ["2", "2", "2", "0", "0", "0", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2", "2", "2", "2"],
        ]
        board = SolitaireBoard(state)
        moves = list(board.possible_moves())
        assert len(moves) == 2

        expected_moves = [
            Move(MoveDirection.LEFT, BoardCoordinate(4, 4)),
            Move(MoveDirection.RIGHT, BoardCoordinate(4, 4)),
        ]
        for actual_move in moves:
            assert actual_move in expected_moves

    def test_identifies_vertical_and_horizontal_move(self):
        state = [
            ["2", "2", "0", "0", "0", "2", "2"],
            ["2", "2", "0", "0", "0", "2", "2"],
            ["0", "0", "0", "0", "0", "1", "1"],
            ["0", "0", "0", "0", "0", "1", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["2", "2", "0", "0", "0", "2", "2"],
            ["2", "2", "0", "0", "0", "2", "2"],
        ]
        board = SolitaireBoard(state)
        moves = list(board.possible_moves())
        assert len(moves) == 2

        expected_moves = [
            Move(MoveDirection.LEFT, BoardCoordinate(6, 2)),
            Move(MoveDirection.DOWN, BoardCoordinate(5, 2)),
        ]
        for actual_move in moves:
            assert actual_move in expected_moves


class TestApplyMove:
    def test_moves_down_correctly(self):
        board = SolitaireBoard()
        down_move = Move(MoveDirection.DOWN, BoardCoordinate(4, 2))

        new_board = board.apply_move(down_move)

        assert new_board.state[2][4] == "0"
        assert new_board.state[3][4] == "0"
        assert new_board.state[4][4] == "1"

    def test_moves_up_correctly(self):
        board = SolitaireBoard()
        down_move = Move(MoveDirection.UP, BoardCoordinate(4, 6))

        new_board = board.apply_move(down_move)

        assert new_board.state[6][4] == "0"
        assert new_board.state[5][4] == "0"
        assert new_board.state[4][4] == "1"

    def test_moves_left_correctly(self):
        board = SolitaireBoard()
        down_move = Move(MoveDirection.LEFT, BoardCoordinate(6, 4))

        new_board = board.apply_move(down_move)

        assert new_board.state[4][6] == "0"
        assert new_board.state[4][5] == "0"
        assert new_board.state[4][4] == "1"

    def test_moves_right_correctly(self):
        board = SolitaireBoard()
        down_move = Move(MoveDirection.RIGHT, BoardCoordinate(2, 4))

        new_board = board.apply_move(down_move)

        assert new_board.state[4][2] == "0"
        assert new_board.state[4][3] == "0"
        assert new_board.state[4][4] == "1"
