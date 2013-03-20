
"""
A demo of A* search algorithm and solution.
"""
"""
This is a simple example of A* Search

http://en.wikipedia.org/wiki/A*_search_algorithm
"""
from pprint import pprint

from algorithms.a_star import a_star_search
from problems.a_star_problem import AStarProblem
from util.maze import NPMaze


if __name__ == '__main__':
    WIDTH = 10
    HEIGHT = 10
    P = (.7, .3)

    # create a maze
    maze = NPMaze(WIDTH, HEIGHT, p=P)
    maze.create_maze()

    problem = AStarProblem(maze)

    print a_star_search(problem, maze.heuristic)
    pprint(maze.maze)
