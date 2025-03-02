from typing import List
from movie import Movie
from enums import Location

class MovieController:
    def __init__(self):
        self.movie_location: dict[Location, List[Movie]] = {}
        self.movies: List[Movie] = []
    
    def add_movie(self, location: Location, movie):
        self.movies.append(movie)
        movies = self.movie_location.get(location) or []
        movies.append(movie)
        self.movie_location[location] = movies
    
    def get_movies_by_location(self, location: Location):
        return self.movie_location.get(location) or []

    def get_movie_by_name(self, name):
        for movie in self.movies:
            if movie.name == name:
                return movie
