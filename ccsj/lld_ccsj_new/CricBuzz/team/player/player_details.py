from team.player.person import Person
from team.player.player_type import PlayerType
from team.player.score import BattingScoreCard, BowllingScoreCard

class PLayerDetails:
    def __init__(self, person: Person, player_type: PlayerType):
        self.person: Person = person
        self.player_type: PlayerType = player_type
        self.batting_score_card: BattingScoreCard = BattingScoreCard()
        self.bowlling_score_card: BowllingScoreCard = BowllingScoreCard()

    def print_batting_score_card(self):
        print(
            f"PlayerName: {self.person.name} -- totalRuns: {self.batting_score_card.total_runs} \
                -- totalBallsPlayed: {self.batting_score_card.total_ball_played} -- 4s: {self.batting_score_card.total_fours} \
                    --  6s: {self.batting_score_card.total_six} -- outby: {None}"
        )

    def print_batting_score_card(self):
        print(
            f"PlayerName: {self.person.name} -- totalOversThrown: {self.bowlling_score_card.total_over_count} \
              -- totalRunsGiven: {self.bowlling_score_card.runs_given} -- WicketsTaken: {self.bowlling_score_card.wicket_taken} "
        )