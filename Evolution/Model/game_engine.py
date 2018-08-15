"""Here each tick gets iterated"""
from bisect import bisect_left
from random import random
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
        self.startingpos_y = -self.board_height/2 + 50
        self.targetpos_x = 0
        self.targetpos_y = self.board_height/2 - 50

        self.pool_size = 200

        self.iteration_max = 1000
        self.iteration_counter = 0
        self.movement_speed = 1

        self.generation = 0
        self.max_fitness = 0
        self.fitness_array = []

        target = Target(self.targetpos_x, self.targetpos_y)
        self.board = Board(self.board_width, self.board_height, target)
        self.pool = [Dot(self.startingpos_x, self.startingpos_y) for i in range(self.pool_size)]

        for dot in self.pool:
            dot.generate_first_generation(self.iteration_max)

    def iterate(self):
        """Increments the timestep by one"""
        self.updating = True
        self.iteration_counter += 1
        for dot in self.pool:
            dot.move(self.board)
        self.updating = False

    def generate_new_generation(self):
        """ Genereates the next generation of dots """
        self.generation += 1
        self.iteration_counter = 0

        self.calculate_fitness_array()
        self.pool = self.breed_generation()

    def calculate_fitness_array(self):
        """ Calculates the fitness array """
        min_distance = self.board_height + self.board_width
        max_distance = 0
        min_time = self.iteration_max
        average_distance = 0
        for dot in self.pool:
            dot.calculate_distance(self.board.target)
            average_distance += dot.distance
            if dot.target_reached_at > 0 and min_time > dot.target_reached_at:
                min_time = dot.target_reached_at
            if min_distance > dot.distance:
                min_distance = dot.distance
            if max_distance < dot.distance:
                max_distance = dot.distance
        average_distance = average_distance/self.pool_size
        print("Aver dist: " + str(average_distance) \
            + "\tMin dist: " + str(min_distance) \
            + "\tMin dist: " + str(max_distance) \
            + "\tMin time: " + str(min_time))

        for dot in self.pool:
            dot.relative_fitness = 1/(dot.distance - min_distance + 1)
            if dot.target_reached_at > 0:
                dot.relative_fitness += 0.1*(self.iteration_max - dot.target_reached_at + 1)

        cumulated_fitness = 0
        self.fitness_array = []
        for dot in self.pool:
            cumulated_fitness += dot.relative_fitness
            self.fitness_array.append(cumulated_fitness)

        self.max_fitness = cumulated_fitness

    def breed_generation(self):
        """Breeds a new generation of dots"""
        new_pool = []
        for dummy in range(self.pool_size):
            random_selector = self.max_fitness*random()
            selected_brood = self.take_closest_index(self.fitness_array, random_selector)
            new_brood = Dot(self.startingpos_x, self.startingpos_y)
            new_brood.movement_directions = self.pool[selected_brood].movement_directions[:]
            new_brood.mutate()
            new_pool.append(new_brood)
        return new_pool

    @staticmethod
    def take_closest_index(sorted_list, number):
        """
        Assumes myList is sorted. Returns closest value to myNumber.

        If two numbers are equally close, return the smallest number.
        """
        pos = bisect_left(sorted_list, number)
        if pos == 0:
            return pos
        if pos == len(sorted_list):
            return pos
        before = sorted_list[pos - 1]
        after = sorted_list[pos]
        if after - number < number - before:
            return pos - 1
        else:
            return pos

    def info_text(self):
        """Returns information about the current iteration/generation"""
        text = ""
        text += "Iteration: " + str(self.iteration_counter) + "\n"
        text += "Generation: " + str(self.generation)
        return text
