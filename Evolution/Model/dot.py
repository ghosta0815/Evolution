"""Class that represents a dot, that gets moved"""
import random
import math
from enum import Enum
from Model.target import Target

class Direction(Enum):
    """Enum that represents directions"""
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Dot():
    """Point on an x-y plain, that moves in a certain pattern"""

    def __init__(self, startpos_x, startpos_y, movement_speed):
        self.fitness = 0
        self.mutation_strength = 0.01

        self.movement_counter = 0
        self.pos_x = startpos_x
        self.pos_y = startpos_y
        self.movement_speed = movement_speed
        self.movement_directions = []

    def generate_first_generation(self, max_movement):
        """Returns directions for the first generation of moving the dot"""
        self.movement_directions = random.choices(list(Direction), k=max_movement)

    def mutate(self):
        """Mutates the Dot's movement_directions"""
        for i in range(len(self.movement_directions)):
            if random.random() < self.mutation_strength:
                self.movement_directions[i] = random.choice(list(Direction))

    def calculate_fitness(self, target):
        """Calculates the fitness based on the distance to a target"""
        self.fitness = math.sqrt((target.pos_x - self.pos_x)**2 + (target.pos_y - self.pos_y)**2)

    def move(self, board):
        """Moves the dot on the board, based on the trained movement directions"""
        if self.movement_counter < len(self.movement_directions):
            movement_direction = self.movement_directions[self.movement_counter]
            self.movement_counter += self.movement_speed
            if movement_direction == Direction.UP:
                self.pos_y += self.movement_speed
                if board.is_outside(self.pos_x, self.pos_y):
                    self.pos_y -= self.movement_speed
            if movement_direction == Direction.RIGHT:
                self.pos_x += self.movement_speed
                if board.is_outside(self.pos_x, self.pos_y):
                    self.pos_x -= self.movement_speed
            if movement_direction == Direction.DOWN:
                self.pos_y -= self.movement_speed
                if board.is_outside(self.pos_x, self.pos_y):
                    self.pos_y += self.movement_speed
            if movement_direction == Direction.LEFT:
                self.pos_x -= self.movement_speed
                if board.is_outside(self.pos_x, self.pos_y):
                    self.pos_x += self.movement_speed


if __name__ == "__main__":
    # pylint: disable=W0212
    DOT = Dot(0, 0, 2)
    print(DOT.generate_first_generation(20))
