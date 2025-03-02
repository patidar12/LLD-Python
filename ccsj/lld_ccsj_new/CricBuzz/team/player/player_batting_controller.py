from typing import List

from team.player import PLayerDetails

class PLayerBattingController:
    def __init__(self, playing_11: List[PLayerDetails]):
        self.yet_to_play: List[PLayerDetails] = playing_11
        self.striker: PLayerDetails = None
        self.non_striker: PLayerDetails = None
    
    def get_next_player(self) -> None:
        if not self.yet_to_play:
            raise Exception("All out...")
        
        if self.striker == None:
            self.striker = self.yet_to_play.pop(0)
        
        if self.non_striker == None:
            self.non_striker = self.yet_to_play.pop(0)
    
    def get_striker(self) -> PLayerDetails:
        return self.striker
    
    def get_non_striker(self):
        return self.non_striker

    def set_striker(self, player: PLayerDetails) -> None:
        self.striker = player

    def set_non_striker(self, player: PLayerDetails) -> None:
        self.non_striker = player
