from typing import List

from movie import Movie
from screen import Screen

class Show:
    def __init__(self, sid: int, start_time: int, movie: Movie, screen: Screen):
        self.id: int = sid
        self.start_time: int = start_time
        self.movie: Movie = movie
        self.screen: Screen = screen
        self.booked_seats: List[int] = []
    

    def set_booked_seats(self, booked_seats: List[int]):
        self.booked_seats.extend(booked_seats)
