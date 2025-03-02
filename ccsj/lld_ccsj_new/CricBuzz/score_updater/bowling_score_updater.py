from inning import BallDetails, BallType, RunType
from score_updater import ScoreUpdaterObesrver


class BowlingScoreUpdater(ScoreUpdaterObesrver):

    def update(self, ball_details: BallDetails):

        if (ball_details.ball_number == 6 and ball_details.ball_type == BallType.NORMAL):
            ball_details.bowled_by.bowlling_score_card.total_over_count += 1

        if (RunType.ONE == ball_details.run_type):
            ball_details.bowled_by.bowlling_score_card.runs_given += 1
        elif (RunType.TWO == ball_details.run_type):
            ball_details.bowled_by.bowlling_score_card.runs_given += 2
        elif (RunType.FOUR == ball_details.run_type):
            ball_details.bowled_by.bowlling_score_card.runs_given += 4
        elif (RunType.SIX == ball_details.run_type):
            ball_details.bowled_by.bowlling_score_card.runs_given += 6

        if (ball_details.wicket != None):
            ball_details.bowled_by.bowlling_score_card.wicket_taken += 1

        if (ball_details.ball_type == BallType.NOBALL):
            ball_details.bowled_by.bowlling_score_card.no_ball_count += 1

        if (ball_details.ball_type == BallType.WIDEBALL):
            ball_details.bowled_by.bowlling_score_card.wide_ball_count += 1
