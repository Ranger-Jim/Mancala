from board import Board
from random import randrange
import sys
import copy

P1_PITS = 0
P1_STORE = 1
P2_PITS = 2
P2_STORE = 3

class Player(object):
    def __init__(self, name="placeholderName"):
        self.name = name

    def __str__(self):
        return "Player: %s" % self.name

    def get_name(self):
        return self.name

class HumanPlayer(Player):
    def __init__(self, number, board, name="HUMAN_NAME"):
        super(HumanPlayer, self).__init__(number, board, name)

    def getNextMove(self):
        try:
            selection = int(input("%s Please input your next move (1 to 6): " % self.name))
            if (selection < 1) or (selection > 6):
                print("Input is out of range (1 to 6)")
                sys.exit()
            return selection-1
        except ValueError:
            print("Input is not an integer")
            sys.exit()

class ComputerPlayer(Player):        
    def __init__(self, board=None, name="COMPUTER_NAME"):
        super(ComputerPlayer, self).__init__(name)
        if board is None:
            self.board = Board()  
        else:
            self.board = Board(board)

    def getNextMove(self):
        selection = randrange(0,6)
        return selection

    def getNextMoveAI(self, player, board=None):
        best_move = None
        best_value = -sys.maxsize
        for move in range(6):
            if board[player- 1][move] > 0:  
                simulated_board, free_move = self.simulate_move(board, player, move)
                value = self.minimax(player, simulated_board, 3, not free_move) 
                if value > best_value:
                    best_value = value
                    best_move = move
        return best_move

    def simulate_move(self, board, player_number, move):
        new_board, free_move, earned_capture = self.board.makeMove(player_number, move, board)
        return new_board, free_move

    def minimax(self, player, board, depth, is_maximizing_player):
        if player == 1:
            pits = 0
        else: 
            pits = 2
        isWinner, currBoard = match.checkForWinner(player, board)
        if depth == 0 or isWinner:
            return self.evaluate(player, board)

        if is_maximizing_player:
            best_value = -sys.maxsize
            for move in range(6): 
                if board[pits][move] > 0:  
                    new_board, free_move = self.simulate_move(board, player, move)
                    value = self.minimax(player, new_board, depth - 1, not free_move)
                    best_value = max(best_value, value)
            return best_value
        else:
            best_value = sys.maxsize
            opponent_number = 2 if player == 1 else 0
            opposite_player = 0 if player == 1 else 1
            for move in range(6):  
                if board[opponent_number][move] > 0:  
                    new_board, free_move = self.simulate_move(board, opposite_player, move)
                    value = self.minimax(opposite_player, new_board, depth - 1, free_move)
                    best_value = min(best_value, value)
            return best_value

    def evaluate(self, player, board):
        return board[P1_STORE][0] - board[P2_STORE][0] if player == 1 else board[P2_STORE][0] - board[P1_STORE][0]

class Match(object):
    def __init__(self, board=None):
        if board is None:
            self.board = Board()  
        else:
            self.board = Board(board)

    def checkMove(self, player, index, curr_board):
        deepCopyOfBoardForAI = copy.deepcopy(curr_board)
        if player == 1:
            pits = 0 
        else: 
            pits = 2
        if index == 10:
            index = computer_player.getNextMove()
            while (deepCopyOfBoardForAI[pits][index] == 0):
                index = computer_player.getNextMove()
        elif index == 100:
            index = computer_player.getNextMoveAI(player, deepCopyOfBoardForAI)
        updated_board, earned_free_move, earned_capture = self.board.makeMove(player, index, curr_board)
        is_game_over, updated_board = self.checkForWinner(player, updated_board)
        return updated_board, earned_free_move, earned_capture, is_game_over 

    def checkForWinner(self, player, curr_board):
        if set(curr_board[P1_PITS]) == set([0]):
            curr_board = self.board.gatherRemaining(player, curr_board)
            return True, curr_board
        elif set(curr_board[P2_PITS]) == set([0]):
            curr_board = self.board.gatherRemaining(player, curr_board)
            return True, curr_board
        else:
            return False, curr_board
    
computer_player = ComputerPlayer()
match = Match()