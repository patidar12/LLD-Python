from abc import ABC, abstractmethod

from inning.ball_details import BallDetails

class ScoreUpdaterObesrver(ABC):

    @abstractmethod
    def update(self, ball_details: BallDetails): pass
