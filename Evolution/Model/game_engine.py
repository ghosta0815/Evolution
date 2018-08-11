"""Here each tick gets iterated"""
from Model.dot import Dot
from Model.board import Board

class GameEngine:
    """Class that is the main Engine"""
    def __init__(self):
        self.startingpos_x = -200
        self.startingpos_y = 0
        self.board_width = 400
        self.board_height = 600
        self.pool_size = 200

        self.iteration_max = 1000
        self.iteration_counter = 0
        self.movement_speed = 1

        self.board = Board(self.board_width, self.board_height)

        self.pool = [Dot(self.startingpos_x, self.startingpos_y, self.movement_speed) \
            for i in range(self.pool_size)]

        for dot in self.pool:
            dot.generate_first_generation(self.iteration_max)

    def iterate(self):
        """Increments the timestep by one"""
        self.iteration_counter += 1
        for dot in self.pool:
            dot.move(self.board)
