from dice import Dice
from board import Board
from player import Player
from cell import Cell

class Game:
    def __init__(self, board_size = 100, snacks = 10, ladders = 10, players = 2, dice = 1):
        self.board = None
        self.players = []
        self.dice = None
        self.initialize_game(board_size, snacks, ladders, players, dice)

    def initialize_game(self, board_size, snacks, ladders, players, dice):
        self.board = Board(board_size, snacks, ladders)
        self.dice = Dice(dice)
        for pnum in range(1, players+1):
            self.players.append(Player(f"p{pnum}"))
    
    def is_win(self, pos):
        if pos >= (self.board.size * self.board.size - 1):
            return True
        return False
    
    def find_player_turn(self):
        player_turn = self.players[0]
        self.players.append(self.players.pop(0))
        return player_turn

    def jump_check(self, player_position):
        if player_position > (self.board.size * self.board.size-1):
            return player_position
        
        cell: Cell = self.board.get_cell(player_position)
        jump = cell.jump
        if jump and jump.start == player_position:
            print(f"Jump By: {jump.name}")
            return jump.end
        return player_position

    def start_game(self):
        while True:
            player_turn: Player = self.find_player_turn()
            print(f"Player {player_turn.pid} Current possition before roll: {player_turn.current_pos}")
            dice_number = self.dice.roll_dice()
            player_new_pos = player_turn.current_pos + dice_number
            player_new_pos = self.jump_check(player_new_pos)
            player_turn.current_pos = player_new_pos
            print(f"Player {player_turn.pid} Current possition after roll: {player_turn.current_pos}")
            if self.is_win(player_turn.current_pos):
                    print(f"Congratulations... Player {player_turn.pid} won the game...")
                    break
            
        

