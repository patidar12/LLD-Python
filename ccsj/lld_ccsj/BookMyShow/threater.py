from typing import List

from screen import Screen
from show import Show
from Enums.city import City

class Threater:
    def __init__(self, threater_id: int, city: City, address: str, screens: List[Screen], shows: List[Show]):
        self.address: str = address
        self.threater_id: int = threater_id
        self.city: City = city
        self.screens: List[Screen] = screens
        self.shows: List[Show] = shows
