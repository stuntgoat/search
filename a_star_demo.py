
"""
A demo of A* search algorithm and solution.
"""
"""
This is a simple example of A* Search

http://en.wikipedia.org/wiki/A*_search_algorithm
"""
from pprint import pprint

# A* algorithm implementation
from algorithms.a_star import a_star_search

# concret problem using a maze
from problems.a_star_problem import AStarProblem

# maze object for the problem
from util.maze import NPMaze


if __name__ == '__main__':
    WIDTH = 10
    HEIGHT = 10
    P = (.7, .3)

    # create a maze
    maze = NPMaze(WIDTH, HEIGHT, p=P)
    maze.create_maze()

    # wrap it in a problem interface
    problem = AStarProblem(maze)

    # solve the problem with the heuristic
    print a_star_search(problem, maze.heuristic)

    # show the maze
    pprint(maze.maze)
