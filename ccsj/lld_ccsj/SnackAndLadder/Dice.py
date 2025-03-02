import random

class Dice:
    MIN: int = 1
    MAX: int = 6
    def __init__(self, dice_count: int = 1):
        self.dice_count = dice_count
    

    def roll_dice(self):
        total_number = 0
        dice_count = self.dice_count
        while dice_count > 0:
            total_number += random.randint(self.MIN, self.MAX)
            dice_count -= 1
        return total_number
