from typing import List

from team.player import PLayerDetails
from team import Team
from inning.ball_type import BallType

class OverDetails:
    def __init__(self, over_number: int, bowled_by: PLayerDetails):
        from inning.ball_details import BallDetails
        self.over_number: int = over_number
        self.bowled_by: PLayerDetails = bowled_by
        self.balls: List[BallDetails] = []
        self.extra_ball_count: int = 0
    
    def start_over(self, batting_team: Team, bowling_team: Team, runs_to_win: int):
        from inning.ball_details import BallDetails
        ball_count: int = 1
        while ball_count <= 6:
            ball: BallDetails = BallDetails(ball_count)
            ball.start_ball_delivery(batting_team, bowling_team, self)
            if(ball.ball_type == BallType.NORMAL):
                self.balls.append(ball)
                ball_count += 1
                if(ball.wicket != None):
                    batting_team.choose_next_batsman()
                if( runs_to_win != -1 and batting_team.get_total_runs() >= runs_to_win):
                    batting_team.is_winner = True
                    return True
            else:
                self.extra_ball_count += 1

        return False
