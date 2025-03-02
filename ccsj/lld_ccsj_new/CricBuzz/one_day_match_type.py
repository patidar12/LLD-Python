from match_type import MatchType

class OneDayMatchType(MatchType):

    def no_of_overs(self):
        return 50

    def max_over_count_per_bowler(self):
        return 10