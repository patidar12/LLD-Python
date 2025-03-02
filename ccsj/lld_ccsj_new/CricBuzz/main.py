from typing import List

from team import Team
from team.player import PLayerDetails, PlayerType, Person
from t_20_match_type import T20MatchType
from match import Match

class Main:

    def main(self):
        ob = Main()

        team_a: Team = ob.__add_team("India")
        team_b: Team = ob.__add_team("SriLanka")

        match_type = T20MatchType()
        match: Match = Match(team_a, team_b, None, "SMS STADIUM", match_type)
        match.start_match()


    def __add_team(self, name: str):
        p1: PLayerDetails = self.__add_player(name+"1", PlayerType.ALLROUNDER)
        p2: PLayerDetails = self.__add_player(name+"2", PlayerType.ALLROUNDER)
        p3: PLayerDetails = self.__add_player(name+"3", PlayerType.ALLROUNDER)
        p4: PLayerDetails = self.__add_player(name+"4", PlayerType.ALLROUNDER)
        p5: PLayerDetails = self.__add_player(name+"5", PlayerType.ALLROUNDER)
        p6: PLayerDetails = self.__add_player(name+"6", PlayerType.ALLROUNDER)
        p7: PLayerDetails = self.__add_player(name+"7", PlayerType.ALLROUNDER)
        p8: PLayerDetails = self.__add_player(name+"8", PlayerType.ALLROUNDER)
        p9: PLayerDetails = self.__add_player(name+"9", PlayerType.ALLROUNDER)
        p10: PLayerDetails = self.__add_player(name+"10", PlayerType.ALLROUNDER)
        p11: PLayerDetails = self.__add_player(name+"11", PlayerType.ALLROUNDER)

        player_details: List[PLayerDetails] = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

        bowlers: List[PLayerDetails] = [p8, p9, p10, p11]

        team: Team = Team(name, player_details, [], bowlers)
        return team

    def __add_player(self, name: str, player_type: PlayerType):
        person: Person = Person()
        person.name = name
        player_details: PLayerDetails = PLayerDetails(person, player_type)
        return player_details


Main().main()