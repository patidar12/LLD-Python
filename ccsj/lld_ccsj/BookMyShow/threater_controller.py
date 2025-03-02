from typing import Dict, List

from Enums.city import City
from threater import Threater
from movie import Movie
from show import Show

class ThreaterController:
    def __init__(self):
        self.city_vs_threater: Dict[City, List[Threater]] = {}
        self.all_threater: List[Threater] = []

    def add_threater(self, threater: Threater, city: City) -> None:
        self.all_threater.append(threater)
        self.city_vs_threater.setdefault(city, [])
        self.city_vs_threater[city].append(threater)

    def get_all_show(self, city: City, movie: Movie) -> Dict[Threater, List[Show]]:
        threater_vs_shows: Dict[Threater, List[Show]] = {}
        for threater in self.city_vs_threater.get(city, []):
            given_movie_shows = []
            for show in threater.shows:
                if show.movie.id == movie.id:
                    given_movie_shows.append(show)
            if given_movie_shows:
                threater_vs_shows[threater] = given_movie_shows
        return threater_vs_shows

