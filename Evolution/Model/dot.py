"""Class that represents a dot, that gets moved"""
import random
import math
from enum import Enum

class Direction(Enum):
    """Enum that represents directions"""
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Dot():
    """Point on an x-y plain, that moves in a certain pattern"""

    def __init__(self, startpos_x, startpos_y):
        self.distance = 0
        self.target_reached_at = -1
        self.relative_fitness = 0
        self.mutation_strength = 0.1

        self.direction_change_propability = 0.5
        self.movement_directions = []

        self.movement_counter = 0
        self.start_pos_x = startpos_x
        self.start_pos_y = startpos_y
        self.pos_x = startpos_x
        self.pos_y = startpos_y
        self.movement_speed = movement_speed

    def generate_first_generation(self, max_movement):
        """Returns directions for the first generation of moving the dot"""
        self.movement_directions = random.choices(list(Direction), k=max_movement)

    def mutate(self):
        """Mutates the Dot's movement_directions"""
        self.pos_x = self.start_pos_x
        self.pos_y = self.start_pos_y
        self.movement_counter = 0
        for i in range(len(self.movement_directions)):
            if random.random() < self.mutation_strength:
                self.movement_directions[i] = random.choice(list(Direction))

    def calculate_distance(self, target):
        """Calculates the fitness based on the distance to a target"""
        self.distance = math.sqrt((target.pos_x - self.pos_x)**2 \
            + (target.pos_y - self.pos_y)**2)

    def move(self, board):
        """Moves the dot on the board, based on the trained movement directions"""
        if self.movement_counter < len(self.movement_directions) and self.target_reached_at == -1:
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
            if board.target_reached(self.pos_x, self.pos_y):
                self.target_reached_at = self.movement_counter

if __name__ == "__main__":
    # pylint: disable=W0212
    DOT = Dot(0, 0)
    print(DOT.generate_first_generation(20))
