from typing import List, Dict
from team.player import PLayerDetails, PLayerBattingController, PlayerBowlingController



class Team:
    def __init__(self, name: str, playing11: List[PLayerDetails], bench: List[PLayerDetails], bowlers: List[PLayerDetails]):
        self.name: str = name
        self.playing11: List[PLayerDetails] = playing11
        self.bench: List[PLayerDetails] = bench
        self.is_winner: bool = False
        self.batting_controller: PLayerBattingController = PLayerBattingController(playing11)
        self.bowling_controller: PlayerBowlingController = PlayerBowlingController(bowlers)
    
    def get_name(self):
        return self.name

    def choose_next_batsman(self):
        self.batting_controller.get_next_player()

    def choose_next_bowler(self, max_over_count_per_bowler):
        self.bowling_controller.get_next_bowler(max_over_count_per_bowler)

    def get_striker(self):
        return self.batting_controller.get_striker()

    def get_non_striker(self):
        return self.batting_controller.get_non_striker()

    def set_striker(self, player: PLayerDetails):
        self.batting_controller.set_striker(player)

    def set_non_striker(self, player: PLayerDetails):
        self.batting_controller.set_non_striker(player)

    def get_current_bowler(self):
        return self.bowling_controller.get_current_bowler()

    def print_batting_score_card(self):
        for player in self.playing11:
            player.print_batting_score_card()

    def get_total_runs(self):
        total_run = 0
        for player in self.playing11:
            total_run += player.batting_score_card.total_runs
        return total_run
