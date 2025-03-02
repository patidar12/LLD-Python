from typing import List

from Model.PieceType import PieceType
from Model.PlayingPieceO import PlayingPieceO
from Model.PlayingPieceX import PlayingPieceX
from Model.Player import Player
from Model.Board import Board

class TicTacToeGame:
    def __init__(self):
        self.players: List[Player] = []
        self.board: Board = None
        self.initialize_game()

    def initialize_game(self):
        piece_x = PlayingPieceX()
        p1 = Player(name="Player 1", piece=piece_x)

        piece_o = PlayingPieceO()
        p2 = Player(name="Player 2", piece=piece_o)

        self.players = [p1, p2]

        self.board = Board(size=3)
    
    def start_game(self):
        '''
        Start game.
        '''
        no_winner: bool = True
        while no_winner:
            self.board.print_board()
            free_cell = self.board.get_free_cell()
            if not free_cell:
                # no winner, this is tie
                no_winner = False
                continue
            player_turn = self.players[0]
            # read the use input:
            row, col = map(int, input(f"Player {player_turn.name} Enter row, column: ").split(','))

            # add piece in board
            piece_added = self.board.add_piece(row, col, player_turn.piece)
            if not piece_added:
                print("Incorrect possition chosen, Please try agiain...")
                continue
            # check winner
            winner = self.isThereWinner(row, col, player_turn.piece.type)
            if winner:
                return player_turn.name
            # remove player from first position and add in last.
            self.players.append(self.players.pop(0))
        return 'tie'

    def isThereWinner(self, row: int, col: int, pieceType: PieceType)->bool:
        # check in row
        isWinner = True
        for i in range(self.board.size):
            if self.board.board[row][i] == None or self.board.board[row][i].type != pieceType:
                isWinner = False
        if isWinner:
            return isWinner

        # check in col
        isWinner = True
        for i in range(self.board.size):
            if self.board.board[i][col] == None or self.board.board[i][col].type != pieceType:
                isWinner = False
        if isWinner:
            return isWinner

        # check in digonal
        isWinner = True
        for i in range(self.board.size):
            if self.board.board[i][i] == None or self.board.board[i][i].type != pieceType:
                isWinner = False
        if isWinner:
            return isWinner

        # check in anti-digonal
        isWinner = True
        for i in range(self.board.size):
            if self.board.board[i][self.board.size-i-1] == None or self.board.board[i][self.board.size-i-1].type != pieceType:
                isWinner = False
        return isWinner
