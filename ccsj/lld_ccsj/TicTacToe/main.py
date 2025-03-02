from TicTacToeGame import TicTacToeGame

class StartGame:
    def start(self):
        tic_tac_toe: TicTacToeGame = TicTacToeGame()
        print("Game winner is: ", tic_tac_toe.start_game())

StartGame().start()