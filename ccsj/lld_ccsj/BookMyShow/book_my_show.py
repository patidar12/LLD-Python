from typing import List

from Enums.city import City
from Enums.seat_category import SeatCategory

from movie_controller import MovieController
from threater_controller import ThreaterController
from movie import Movie
from seat import Seat
from screen import Screen
from show import Show
from threater import Threater

class BookMyShow:
    def __init__(self):
        self.movi_controller: MovieController = MovieController()
        self.threater_controller: ThreaterController = ThreaterController()
    
    def initialize(self):
        self.create_movies()
        self.create_threater()

    
    def create_booking(user_city: City, movie_name: str):
        # TODO: will be done latter
        pass

    def create_threater(self):
        avengers: Movie = self.movi_controller.get_movie_by_name("Avengers")
        baahubali: Movie = self.movi_controller.get_movie_by_name("Bahubali")
        #__init__(self, threater_id: int, city: City, address: str, screens: List[Screen], shows: List[Show]):
        screens = self.create_screens()
        morning_show = self.create_show(1, avengers, screens[0], 9)
        evening_show = self.create_show(2, baahubali, screens[0], 16)
        shows: List[Show] = [morning_show, evening_show]
        inox_threater = Threater(1, City.BANGALORE, "Jayanagar", screens, shows)

        screens = self.create_screens()
        morning_show = self.create_show(3, avengers, screens[0], 13)
        evening_show = self.create_show(4, baahubali, screens[0], 20)
        shows: List[Show] = [morning_show, evening_show]
        pvr_threater = Threater(2, City.DELHI, "India Gate", screens, shows)
        self.threater_controller.add_threater(inox_threater, City.BANGALORE)
        self.threater_controller.add_threater(pvr_threater, City.DELHI)

    def create_movies(self):
        avengers: Movie = Movie(1, "Avengers", 150)
        baahubali: Movie = Movie(2, "Bahubali", 180)
        self.movi_controller.add_movie(avengers, City.BANGALORE)
        self.movi_controller.add_movie(avengers, City.DELHI)
        self.movi_controller.add_movie(baahubali, City.BANGALORE)


    def create_show(self, show_id: int, movie: Movie, screen: Screen, start_time: int) -> Show:
        return Show(show_id, start_time, movie, screen)

    def create_screens(self):
        screens: List[Screen] = []
        screen = Screen(1, self.create_seats())
        screens.append(screen)
        return screens

    def create_seats(self):
        seats: List[Seat] = []
        
        # 1 to 40 is silver
        for i in range(40):
            seat = Seat(i, SeatCategory.SILVER)
            seats.append(seat)

        # 40 to 70 is gold
        for i in range(40, 70):
            seat = Seat(i, SeatCategory.GOLD)
            seats.append(seat)

        # 70 to 100 is platinum
        for i in range(70, 100):
            seat = Seat(i, SeatCategory.PLATINUM)
            seats.append(seat)
        return seats
