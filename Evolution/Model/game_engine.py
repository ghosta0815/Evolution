"""Here each tick gets iterated"""
from Model.dot import Dot
from Model.board import Board
from Model.target import Target

class GameEngine:
    """Class that is the main Engine"""
    def __init__(self):
        self.updating = False
        self.board_width = 400
        self.board_height = 500

        self.startingpos_x = 0
        self.startingpos_y = -self.board_height/2 + 10
        self.targetpos_x = 0
        self.targetpos_y = self.board_height/2 - 10

        self.pool_size = 200

        self.iteration_max = 200
        self.iteration_counter = 0
        self.movement_speed = 1

        self.generation = 0

        self.board = Board(self.board_width, self.board_height)
        self.target = Target(self.targetpos_x, self.targetpos_y)
        self.pool = [Dot(self.startingpos_x, self.startingpos_y, self.movement_speed) \
            for i in range(self.pool_size)]

        for dot in self.pool:
            dot.generate_first_generation(self.iteration_max)

    def iterate(self):
        """Increments the timestep by one"""
        self.updating = True
        self.iteration_counter += 1
        for dot in self.pool:
            dot.move(self.board)
        self.updating = False

    def info_text(self):
        """Returns information about the current iteration/generation"""
        text = ""
        text += "Iteration: " + str(self.iteration_counter) + "\n"
        text += "Generation: " + str(self.generation)
        return text
