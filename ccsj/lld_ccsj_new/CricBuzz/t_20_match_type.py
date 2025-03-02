from match_type import MatchType

class T20MatchType(MatchType):

    def no_of_overs(self):
        return 20

    def max_over_count_per_bowler(self):
        return 5