from score_updater import ScoreUpdaterObesrver
from inning import BallDetails, RunType

class BattingScoreUpdater(ScoreUpdaterObesrver):

    def update(self, ball_details: BallDetails):
        run = 0
        if (RunType.ONE == ball_details.run_type):
            run = 1
        elif (RunType.TWO == ball_details.run_type):
            run = 2
        elif (RunType.FOUR == ball_details.run_type):
            run = 4
            ball_details.played_by.batting_score_card.total_fours += 1
        elif (RunType.SIX == ball_details.run_type):
            run = 6
            ball_details.played_by.batting_score_card.total_six += 1
        ball_details.played_by.batting_score_card.total_runs += run

        ball_details.played_by.batting_score_card.total_ball_played += 1

        if (ball_details.wicket != None):
            ball_details.played_by.batting_score_card.wicket_details = ball_details.wicket
