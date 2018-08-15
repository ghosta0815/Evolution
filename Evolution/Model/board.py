"""This file contains the board of the game"""

class Board():
    """The class that represents the game board"""
    def __init__(self, width, height, target):
        self.width = width
        self.height = height
        self.target = target

    def is_outside(self, x, y):
        """Returns true if the point is outside of the movable area"""
        if x > self.width/2:
            return True
        if x < -self.width/2:
            return True
        if y > self.height/2:
            return True
        if y < -self.height/2:
            return True
        return False
