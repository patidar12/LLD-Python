from Game import Game

class GameHandler:
    def __init__(self):
        self.game = self.create_game()

    def create_game(self):
        return Game(board_size = 10, snaks = 5, ladders = 5, players = 2, dice_count = 1)

    def start_game(self):
        self.game.start_game()

gm = GameHandler()
gm.start_game()
