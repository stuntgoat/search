"""
A demo of A* search algorithm and solution.
"""
"""
This is a simple example of A* Search

http://en.wikipedia.org/wiki/A*_search_algorithm
"""
from Queue import PriorityQueue

from util import path_from_start


def a_star_search(problem, heuristic):
    """
    Accepts an AStarProblem; see problems/a_star_problem.py
    heuristic is a function from states in the problem to real values such that heuristic(s) underestimates the cost to the nearest goal

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
        print 'cur_node_cost, cur_node', cur_node_cost, cur_node

        # check if this is the goal node
        if problem.goal_test(cur_node):
            return path_from_start(cur_node, parent_map)

        # if not, acquire the list of actions for that state.
        actions = problem.actions(cur_node)  # [(2, node1), (4, node2)]

        parent_heuristic_cost = heuristic(cur_node)
        print 'parent_heuristic_cost', parent_heuristic_cost

        for action in actions:
            transition_cost, child_node = action ####
            print 'transition_cost, child_node', transition_cost, child_node

            # don't explore nodes more than once
            if child_node in explored_nodes:
                continue

            child_heuristic_cost = heuristic(child_node)

            # create a map from the child to the current node
            parent_map[child_node] = cur_node
            current_cost = cur_node_cost - parent_heuristic_cost + transition_cost + child_heuristic_cost

            pq.put((current_cost, child_node))

        # put the current node on the list of explored, once we have
        # explored the available actions for this node
        explored_nodes.add(cur_node)

    # goal not found
    return None


            # f(n) = g(n) + h(n) = "backwards cost" + "forward cost"
            # suppose "parent" of n is m.. transitioncost = cost of going from m to n
            # path taken to get to n = m1 -> m2 -> m3 ... -> x -> m
            # g(n) = tc(m1, m2) + tc(m2, m3) + .... + tc(x, m)
            #
            # suppose m is the node we visited immediately before n.. "m parent of n"
            # f(n) = .... f(m) ...
            # f(n) = g(n) + h(n)
            # f(n) = g(m)[start state to m] + transition(m -> n)[m to n] + h(n)[heuristic from n to goal]
            #
            # f(m) = g(m) + h(m) << by definition
            # f(m) - h(m) = g(m) + h(m) - h(m)
            # f(m) - h(m) = g(m) + 0
            # g(m) = f(m) - h(m) << by algebra from previous line
            #
            # line 59 and line 64:
            # f(n) = g(m) + tc(m -> n) + h(n)     << line 59
            # f(n) = (f(m) - h(m))[g(m)] + tc(m -> n) + h(n)   << using expression of g(m) from line 64

            # f(n) are the priorities in the PQ

            # h(m) =
            # tc(m -> n) =
            # h(n) =
            # f(m) = "priority of m in the PQ"
