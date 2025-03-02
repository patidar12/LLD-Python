from Player import Player
from Dice import Dice
from Board import Board
from Cell import Cell
from Jump import Jump

class Game:
    def __init__(self, board_size: int = 100, snaks: int = 10, ladders: int = 10, players: int = 2, dice_count: int = 1):
        self.board = None
        self.players = None
        self.dice = None
        self.initialize_game(board_size, snaks, ladders, players, dice_count)

    def initialize_game(self, board_size, snaks, ladders, players, dice_count):
        self.board = Board(board_size, snaks, ladders)
        self.dice = Dice(dice_count)
        self.players = []
        for player_id in range(1, players+1):
            player = Player(player_id)
            self.players.append(player)
    
    def is_win(self, current_possition):
        if current_possition >= self.board.size * self.board.size:
           return True
    
    def find_player_turn(self):
        self.players.append(self.players.pop(0))
        return self.players[0]
    
    def jump_check(self, player_possition):
        if player_possition > (self.board.size * self.board.size) - 1:
            return player_possition

        cell: Cell =  self.board.get_cell(player_possition)
        jump: Jump = cell.jump
        if jump and jump.start == player_possition:
            print(f"Jump By: {jump.name}")
            player_possition = jump.end
        return player_possition

    
    def start_game(self):
        while True:
            # find player turn
            player_turn: Player = self.find_player_turn()
            print(f"Player {player_turn.pid} Current possition before roll: {player_turn.current_possition}")

            # roll dice
            dice_number = self.dice.roll_dice()

            # get the new possition
            player_new_possition =  player_turn.current_possition + dice_number
            player_new_possition = self.jump_check(player_new_possition)
            player_turn.current_possition = player_new_possition

            print(f"Player {player_turn.pid} Current possition after roll: {player_turn.current_possition}")

            # check for winning condition
            if self.is_win(player_turn.current_possition):
                print(f"Congratulations... Player {player_turn.pid} won the game...")
                break
            self.players.append(self.players.pop(0))
