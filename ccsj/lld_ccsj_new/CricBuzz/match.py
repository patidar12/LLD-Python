from typing import List
from datetime import date
from random import random

from team import Team
from match_type import MatchType
from inning import InningDetails

class Match:
    def __init__(self, team_a: Team, team_b: Team, match_date: date, venue: str, match_type: MatchType):
        self.team_a: Team = team_a
        self.team_b: Team = team_b
        self.match_date: date = match_date
        self.venue: str = venue
        self.match_type: MatchType = match_type
        self.innings: List[InningDetails] = [None] * 2
    
    def start_match(self):
        # 1. Toss
        toss_winner: Team = self.__toss(self.team_a, self.team_b)

        # start The Inning, there are 2 innings in a match
        for inning in range(1, 3):
            inning_details: InningDetails = None
            bowling_team: Team = None
            batting_team: Team = None

            # assuming here that tossWinner batFirst
            is_chasing: bool = False # no use case, keeping if anything comes in mind latter
            if(inning == 1):
                batting_team = toss_winner
                bowling_team = self.team_b if toss_winner.get_name() == self.team_a.get_name() else self.team_a
                inning_details = InningDetails(batting_team, bowling_team, self.match_type)
                inning_details.start(-1)
            else:
                bowling_team = toss_winner
                batting_team = self.team_b if toss_winner.get_name() == self.team_a.get_name() else self.team_a
                inning_details = InningDetails(batting_team, bowling_team, self.match_type)
                inning_details.start(self.innings[0].get_total_runs())
                if(bowling_team.get_total_runs() > batting_team.get_total_runs()):
                    bowling_team.is_winner = True


            self.innings[inning-1] = inning_details

            # print inning details
            print()
            print(f"INNING: {inning} -- total Run: {batting_team.get_total_runs()}")
            print(f"---Batting ScoreCard: {batting_team.name}---")
            batting_team.print_batting_score_card()
            print()
            print(f"---Bowling ScoreCard: {bowling_team.name}---")
            bowling_team.print_batting_score_card()

        print()
        if(self.team_a.is_winner):
            print(f"---WINNER--- : {self.team_a.name}")
        else:
            print(f"---WINNER--- : {self.team_b.name}")

    def __toss(self, team_a: Team, team_b: Team):
        # random function return value between 0 and 1
        if round(random(), 2) < 0.5:
            return team_a
        else:
            return team_b
