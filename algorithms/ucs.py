"""
This is a simple example of Uniform Cost Search.

http://en.wikipedia.org/wiki/Uniform-cost_search
"""
from Queue import PriorityQueue

from util import path_from_start


def uniform_cost_search(problem):
    """
    Accepts a UCSProblem; see problems/ucs_problem.py.

    Returns a path to goal, or None if a goal is not found.
    """
    pq = PriorityQueue()

    init_cost, init_node = problem.initial_state()
    # put start state on the priority queue
    pq.put((init_cost, init_node))

    parent_map = {}
    explored_nodes = set()

    while not pq.empty():
        # pop node off of the priority queue
        cur_node_cost, cur_node = pq.get()

        # check if this is the goal node
        if problem.goal_test(cur_node):
            return path_from_start(cur_node, parent_map)
        print 'tried', cur_node.name
        # if not, acquire the list of actions for that state.
        actions = problem.actions(cur_node)  # [(2, node1), (4, node2)]

        for action in actions:
            transition_cost, child_node = action

            # don't explore nodes more than once
            if child_node in explored_nodes:
                continue

            # create a map from the child to the current node
            parent_map[child_node] = cur_node
            print 'queueing', child_node.name
            # place each child node on the priority queue
            pq.put((cur_node_cost + transition_cost, child_node))

        # put the current node on the list of explored, once we have
        # explored the available actions for this node
        explored_nodes.add(cur_node)

    # goal not found
    return None
