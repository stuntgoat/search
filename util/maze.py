"""
Generate mazes with have an interface for moving an
finding a path.
"""
from itertools import product
from math import sqrt
np = None
try:
    import numpy as np
except ImportError:
    from random import choice

class MoveException(Exception):
    pass

class NPMaze(object):
    def __init__(self, width, height, goal=5, values=[0, 1], p=[.7, .3]):
        self.width = width
        self.height = height
        self.values = values
        self.p = p
        self.maze = None
        self.goal = goal
        self._goal_coordinates = (width - 1, height - 1)
        self._start_coordinates = (0, 0)
        self._free_cell = values[0]
        self._obstacle_cell = values[1]
        self._move_range = [-1, 0, 1]

    def available_moves(self, coordinates):
        moves = []
        x, y = coordinates
        for move in product(self._move_range, repeat=2):
            add_x, add_y = move
            if add_x == 0 and  add_y == 0:
                continue
            proposed_x = add_x + x
            proposed_y = add_y + y
            proposed_coordinate = (proposed_x, proposed_y)
            if self._available_moves(proposed_coordinate):
                moves.append(proposed_coordinate)
        return moves

    def heuristic(self, coordinates):
        """
        Calculate the hypotenuse from
        """
        x, y = coordinates
        goalx, goaly = self.end
        return sqrt((goalx - x)**2 + (goaly - y)**2)


    def _available_moves(self, coordinates):
        """
        Returns a list of coordinates that are free cells and their
        cost.
        """
        x, y = coordinates
        if x < 0 or y < 0:
            return False

        if x > self.width - 1 or y > self.height - 1:
            return False

        if self.maze[y][x] in (self._free_cell, self.goal):
            return True

        return False

    @property
    def start(self):
        return self._start_coordinates

    @property
    def end(self):
        return self._goal_coordinates

    def create_maze(self):
        if np:
            self.maze = np.random.choice(self.values, (self.height, self.width), p=self.p)
            print 'NUMPY'
        else:
            _free, _obstacles = self.p
            free, obstacles = int(_free * 10), int(_obstacles * 10)
            population = [self._free_cell] * free + [self._obstacle_cell] * obstacles
            self.maze = [[choice(population) for _val in range(self.width)] for _row in range(self.height)]

        # set start
        self.maze[0][0] = 0

        # set goal
        self.maze[self.height - 1][self.width - 1] = self.goal

        print self.maze

    @property
    def goal_coordinates(self):
        """
        Returns a cached version of the goal coordinates
        """
        if not self._goal_coordinates:
            for irow, row in enumerate(self.maze):
                for ival, val in enumerate(row):
                    if val == self.goal_value:
                        self._goal_coordinates = (irow, ival)
        return self._goal_coordinates
