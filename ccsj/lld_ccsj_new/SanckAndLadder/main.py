from game import Game

class GameHandler:
    def __init__(self):
        self.game = self.create_game()

    def create_game(self):
        return Game(board_size = 10, snacks = 5, ladders = 5, players = 2, dice = 1)

    def start_game(self):
        self.game.start_game()

gm = GameHandler()
gm.start_game()
