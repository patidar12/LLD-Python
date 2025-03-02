from typing import Dict, List
from movie import Movie
from Enums.city import City

class MovieController:
    def __init__(self):
        self.city_vs_movies: Dict[City, List[Movie]] = {}
        self.all_movies: List[Movie] = []
    
    def add_movie(self, movie: Movie, city: City) -> None:
        self.all_movies.append(movie)
        if not self.city_vs_movies.get(city):
            self.city_vs_movies[city] = []
        self.city_vs_movies[city].append(movie)
    
    def get_movie_by_name(self, movie_name: str) -> Movie:
        for movie in self.all_movies:
            if movie.name == movie_name:
                return movie
    

    def get_movies_by_city(self, city: str) -> List[Movie]:
        return self.all_movies.get(city, [])
