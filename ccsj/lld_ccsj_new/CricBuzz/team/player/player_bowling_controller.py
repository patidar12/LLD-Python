from typing import List, Dict

from team.player import PLayerDetails

class PlayerBowlingController:
    def __init__(self, bowelers: List[PLayerDetails]):
        self.bowelers: List[PLayerDetails] = []
        self.bowelers_vs_over_count: Dict[PLayerDetails, int] = {}
        self.current_boweler: PLayerDetails = None
        self.set_bowler_list(bowelers)
    
    def set_bowler_list(self, bowelers: List[PLayerDetails]):
        for boweler in bowelers:
            self.bowelers.append(boweler)
            self.bowelers_vs_over_count[boweler] = 0
    
    def get_next_bowler(self, max_over_count_per_bowler: int):
        player_details: PLayerDetails = self.bowelers.pop(0)
        if(self.bowelers_vs_over_count.get(player_details) + 1 == max_over_count_per_bowler):
            self.current_boweler = player_details
        else:
            self.current_boweler = player_details
            self.bowelers.append(player_details)
            self.bowelers_vs_over_count[player_details] = self.bowelers_vs_over_count[player_details] + 1
    
    def get_current_bowler(self):
        return self.current_boweler
