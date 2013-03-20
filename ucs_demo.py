"""
A demo of Uniform Cost Search and solution.
"""
from random import choice

from pytries import WeightedGraph

from algorithms import uniform_cost_search
from problems import UCSProblem


if __name__ == '__main__':
    NODES = 25
    EDGES = 4
    WEIGHT_RANGE = [1, 20]

    # create a weighted graph
    wg = WeightedGraph(edges=EDGES, nodes=NODES, weight_range=[1, 5])
    wg.expand_tree()

    # select a random node at the lowest depth of the graph
    random_node = choice(wg.nodes_at_level(2))
    random_node.is_goal = True
    random_node.cost = 0

    wg.printer()
    print random_node, 'is the goal'

    # create a problem using the weighted graph
    problem = UCSProblem(wg)

    # solve the problem using uniform cost search algorithm
    solution = uniform_cost_search(problem)
    print solution
