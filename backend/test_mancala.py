from mancala import Match, HumanPlayer, ComputerRandomPlayer
from unittest.mock import patch

def test_human_player_init():
    player = HumanPlayer(1, None, "Global")
    assert player.number == 1
    assert player.board is None
    assert player.name == "Global"

def test_human_player_get_next_move():
    with patch('builtins.input', return_value="4"):
        player = HumanPlayer(1, None)
        assert player.getNextMove() == 3  

def test_computer_random_player_init():
    player = ComputerRandomPlayer(2, None)
    assert player.number == 2
    assert player.board is None
    assert player.name == "computer"

def test_computer_random_player_get_next_move():
    with patch('mancala.randrange', return_value=2):
        player = ComputerRandomPlayer(2, None)
        assert player.getNextMove() == 2

def test_match_init():
    with patch('builtins.input', side_effect=['Global', '4']):
        match = Match(HumanPlayer, ComputerRandomPlayer)
        assert isinstance(match.player1, HumanPlayer)
        assert isinstance(match.player2, ComputerRandomPlayer)
        assert match.current_turn == match.player1
        assert match.player1.name == 'Global'
        assert match.player2.name == 'computer'

# def test_make_move_no_free_move():
#     with patch('mancala.Match.checkForWinner', return_value=False):
#         with patch('builtins.input', side_effect=['Global', '4']):
#             with patch('board.Board.makeMove', side_effect=[(['4'] * 10, False)]):
#                 match = Match(HumanPlayer, ComputerRandomPlayer)
#                 match.checkMove()
#                 assert match.current_turn != match.player1

def test_swap_current_turn():
    with patch('builtins.input', side_effect=['Global', '4']):
        match = Match(HumanPlayer, ComputerRandomPlayer)
        initial_turn = match.current_turn
        new_turn = match.swapCurrentTurn()
        assert new_turn == match.player2
        assert match.current_turn == match.player2
        assert match.current_turn != initial_turn

def test_check_for_winner_player1_wins():
    with patch('builtins.input', side_effect=['Global', '4']):
        with patch('mancala.Board.gatherRemaining') as mock_gather_remaining:
            mock_gather_remaining.return_value = [[0] * 6, [0], [0] * 6, [0]]
            match = Match(HumanPlayer, ComputerRandomPlayer)
            match.board.board = [[0] * 6, [0], [0, 0, 0, 0, 0, 1], [0]]  
            result = match.checkForWinner()
            assert result is True 
            assert match.board.board[0] == [0] * 6
            assert match.board.board[1] >= match.board.board[3]
            
def test_check_for_winner_player2_wins():
    with patch('builtins.input', side_effect=['Global', '4']):
        with patch('mancala.Board.gatherRemaining') as mock_gather_remaining:
            mock_gather_remaining.return_value = [[0] * 6, [0], [0] * 6, [0]]
            match = Match(HumanPlayer, ComputerRandomPlayer)
            match.board.board = [[0, 0, 0, 0, 0, 1], [0], [0] * 6, [0]]  
            result = match.checkForWinner()
            assert result is True 
            assert match.board.board[2] == [0] * 6
            assert match.board.board[1] <= match.board.board[3]