"""This file contains the board of the game"""

class Rectangle():
    """This class contains the coordinates of a rectangle

    It is inteded to be used as obstacle in the board class"""
    def __init__(self, left, top, right, bot):
        self.left = left
        self.top = top
        self.right = right
        self.bot = bot

    def inside_rect(self, pos_x, pos_y):
        """Returns true if the point is inside the rectangle object"""
        if pos_x > self.left and pos_x < self.right and pos_y > self.bot and pos_y < self.top:
            return True
        return False

class Board():
    """The class that represents the game board"""
    def __init__(self, width, height, target):
        self.width = width
        self.height = height
        self.target = target
        self.obstacles = []
        self.obstacles.append(Rectangle(-40, -140, 80, -180))
        self.obstacles.append(Rectangle(-200, 0, 40, -20))

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

        for obstacle in self.obstacles:
            if obstacle.inside_rect(x, y):
                return True

        return False

    def target_reached(self, pos_x, pos_y):
        """Returns true, if the target was reached"""
        if abs(pos_x - self.target.pos_x) < 3 and abs(pos_y - self.target.pos_y) < 3:
            return True
        return False
