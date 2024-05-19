from constants import DEFAULT_NAME, P1_PITS, P2_PITS, P1_STORE, P2_STORE
from board import Board
from unittest.mock import patch

def test_board_init_default_values():
    board = Board()
    assert board.board == [[4, 4, 4, 4, 4, 4], [0], [4, 4, 4, 4, 4, 4], [0]]

def test_board_init_with_test_state():
    custom_state = [[1, 1, 1, 1], [0], [2, 2, 2, 2], [0]]
    board = Board(test_state=custom_state)
    assert board.board == custom_state

def test_print_board():
    custom_state = [[1, 2, 3, 4, 5, 6], [0], [1, 2, 3, 4, 5, 6], [0]]
    board = Board(test_state=custom_state)
    expected_output = "   6  5  4  3  2  1\n 0                    0\n   1  2  3  4  5  6\n"
    assert board.printBoard() == expected_output

# def test_makeMove():

def test_getNextArea():
    board = Board()
    assert board.getNextArea(P1_PITS) == P1_STORE
    assert board.getNextArea(P1_STORE) == P2_PITS
    assert board.getNextArea(P2_PITS) == P2_STORE
    assert board.getNextArea(P2_STORE) == P1_PITS

# def test_earnedCapture():

# def stealStones():

def test_getOpposingAreaAndIndex():
    board = Board()
    assert board.getOpposingAreaAndIndex(P1_PITS, 0) == (P2_PITS, 5)
    assert board.getOpposingAreaAndIndex(P2_PITS, 0) == (P1_PITS, 5)
    assert board.getOpposingAreaAndIndex(P1_STORE, 0) == (P2_STORE, 5)
    assert board.getOpposingAreaAndIndex(P2_STORE, 0) == (P1_STORE, 5)

def test_gatherRemaining():
    board = Board()
    assert board.gatherRemaining(1)[0] == [0, 0, 0, 0, 0, 0]
    assert board.gatherRemaining(2)[2] == [0, 0, 0, 0, 0, 0]