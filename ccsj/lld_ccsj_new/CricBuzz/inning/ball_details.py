from typing import List
from random import random

#from inning import BallType, RunType, OverDetails
from inning.ball_type import BallType
from inning.run_type import RunType
from inning.over_details import OverDetails
from team.player import PLayerDetails
from team import Wicket, Team, WicketType

class BallDetails:
    def __init__(self, ball_number: int):
        from score_updater import ScoreUpdaterObesrver, BattingScoreUpdater, BowlingScoreUpdater
        self.ball_number = ball_number
        self.ball_type: BallType = None
        self.run_type: RunType = None
        self.played_by: PLayerDetails = None
        self.bowled_by: PLayerDetails = None
        self.wicket: Wicket = None
        self.score_updater_observer_list: List[ScoreUpdaterObesrver] = [
            BowlingScoreUpdater(),
            BattingScoreUpdater()
        ]

    def start_ball_delivery(self, batting_team: Team, bowling_team: Team, over: OverDetails):
        self.played_by = batting_team.get_striker()
        self.bowled_by = over.bowled_by
        # THROW BALL AND GET THE BALL TYPE, assuming here that ball type is always NORMAL
        self.ball_type = BallType.NORMAL

        # wicket or no wicket
        if (self.__is_wicket_taken()):
            self.run_type = RunType.ZERO
            # considering only BOLD
            self.wicket = Wicket(WicketType.BOLD, bowling_team.get_current_bowler(), over, self)
            # making only striker out for now
            batting_team.set_striker(None)
        else:
            self.run_type = self.__get_run_type()
            if(self.run_type == RunType.ONE or self.run_type == RunType.THREE):
                # swap striket and non striker
                temp: PLayerDetails = batting_team.get_striker()
                batting_team.set_striker(batting_team.get_non_striker())
                batting_team.set_non_striker(temp)

        # update player scoreboard
        self.__notify_updaters()

    def __notify_updaters(self):
        for observer in self.score_updater_observer_list:
            observer.update(self)

    @staticmethod
    def __get_run_type():
        val = round(random(), 2)
        if (val <= 0.2):
            return RunType.ONE
        elif (val >= 0.3 and val <= 0.5):
            return RunType.TWO
        elif (val >= 0.6 and val <= 0.8):
            return RunType.FOUR
        else:
            return RunType.SIX

    @staticmethod
    def __is_wicket_taken():
        # random function return value between 0 and 1
        if (round(random(), 2) < 0.2):
            return True
        else:
            return False
