from typing import List
from enums import Location
from screen import Screen
from show import Show

class Threater:
    def __init__(self, thid, address, location, screens: List[Screen]):
        self.thid = thid
        self.address = address
        self.location: Location = location
        self.screens: List[Screen] = screens
        self.shows: List[Show] = []
    
    def set_show(self, show):
        self.shows.append(show)
    
    def get_shows(self):
        return self.shows
