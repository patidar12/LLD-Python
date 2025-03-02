from typing import List, Dict
from enums import Location
from threater import Threater
from movie import Movie
from show import Show

class ThreaterController:
    def __init__(self):
        self.threater_location: Dict[Location, List[Threater]] = {}
        self.threaters: List[Threater] = []

    def add_threater(self, location: Location, threater: Threater):
        self.threaters.append(threater)
        threaters = self.threater_location.get(location) or []
        threaters.append(threater)
        self.threater_location[location] = threaters

    def get_all_show(self, location: Location, movie: Movie) -> Dict[Threater, List[Show]]:
        threater_vs_shows: Dict[Threater, List[Show]] = {}
        for threater in self.threater_location.get(location, []):
            given_movie_shows = []
            for show in threater.shows:
                if show.movie.mid == movie.mid:
                    given_movie_shows.append(show)
            if given_movie_shows:
                threater_vs_shows[threater] = given_movie_shows
        return threater_vs_shows
