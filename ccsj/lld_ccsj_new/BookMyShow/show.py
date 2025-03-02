from typing import List
from datetime import datetime, timedelta
from movie import Movie
from screen import Screen
from seat import Seat

class Show:
    def __init__(self, sid: int, movie: Movie, screen: Screen, start_time: datetime):
        self.id = sid
        self.movie = movie
        self.screen = screen
        self.start_time: datetime = start_time
        self.end_time: datetime = start_time + timedelta(minutes=self.movie.duration_minutes) 
        self.booked_seats: List[Seat] = []
    
    def set_booked_seats(self, seats: List[Seat]):
        self.booked_seats.extend(seats)

