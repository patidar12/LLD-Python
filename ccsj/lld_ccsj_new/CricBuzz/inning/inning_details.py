from typing import List

from team import Team
from team.player import PLayerDetails
from match_type import MatchType
from inning import OverDetails

class InningDetails:
    def __init__(self, batting_team: Team, bowling_team: Team, match_type: MatchType):
        self.batting_team: Team = batting_team
        self.bowling_team: Team = bowling_team
        self.match_type: MatchType = match_type
        self.overs: List[OverDetails] = []

    def start(self, runs_to_win: int):
        # set batting players
        try:
            self.batting_team.choose_next_batsman()
        except Exception as e:
            pass

        no_of_overs = self.match_type.no_of_overs()
        for over_number in range(1, no_of_overs+1):
            # chooseBowler
            self.bowling_team.choose_next_bowler(self.match_type.max_over_count_per_bowler())

            over: OverDetails = OverDetails(over_number, self.bowling_team.get_current_bowler())
            self.overs.append(over)
            try:
                won: bool = over.start_over(self.batting_team, self.bowling_team, runs_to_win)
                if won == True:
                   break
            except Exception as e:
                break

            # swap striket and non striker
            temp: PLayerDetails = self.batting_team.get_striker()
            self.batting_team.set_striker(self.batting_team.get_non_striker())
            self.batting_team.set_non_striker(temp)

    def get_total_runs(self):
       return self.batting_team.get_total_runs()
