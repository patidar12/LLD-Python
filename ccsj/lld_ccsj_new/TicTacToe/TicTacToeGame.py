from typing import List
from models.board import Board
from models.player import Player
from models.playng_piece import PlayingPieceO, PlayingPieceX

class TicTacToeGame:
    def __init__(self):
        self.players: List[Player] = []
        self.board: Board  = None
        self.initialize_game()

    def initialize_game(self):
        p1 = Player(name="player1", piece=PlayingPieceX())
        p2 = Player(name="player2", piece=PlayingPieceO())
        self.players: List[Player] = [p1, p2]
        self.board = Board(3)

    def is_winner(self, row, col, player: Player):
        is_winner = True
        for i in range(self.board.size):
            if self.board.board[row][i] != player.piece:
                is_winner =  False
                break
        if is_winner: return True
        is_winner = True
        for i in range(self.board.size):
            if self.board.board[i][col] != player.piece:
                is_winner =  False
                break
        if is_winner: return True
        is_winner = True
        for i in range(self.board.size):
            if self.board.board[i][i] != player.piece:
                is_winner = False
                break
        if is_winner: return True
        is_winner = True
        for i in range(self.board.size):
            if self.board.board[i][self.board.size-i-1] != player.piece:
                is_winner = False
                break
        return is_winner
    
    def start_game(self):
        no_winner = True
        while no_winner:
            self.board.print_board()
            player = self.players[0]
            cell = self.board.get_free_cell()
            if not cell:
                print("Match Draw")
                no_winner = False
                continue
            row, col = map(int, input(f"Player {player.name} Enter row, column: ").split(','))
            is_added = self.board.add_piece(row, col, player.piece)
            print("added")
            if not is_added:
                print("Please enter correct position.")
                continue
            print("winner")
            if self.is_winner(row, col, player):
                print(f"Player: {player.name} won the game...")
                no_winner = False
            else:
                print("else")
                self.players.pop(0)
                self.players.append(player)


TicTacToeGame().start_game()