"""
Accepts a WeightedGraph object with a goal node and provides
the interface to the Uniform Cost Search algorithm.
"""

class UCSProblem(object):
    def __init__(self, tree):
        self.tree = tree

    def initial_state(self):
        """
        Returns the root node or starting state.
        """
        return self.tree.root_node.cost, self.tree.root_node

    def actions(self, node):
        """
        Returns a list of child nodes and their edge costs, if available.
        """
        return [(_n.cost, _n) for _n in node.children]

    def goal_test(self, node):
        """
        Returns boolean if the node is the goal.
        """
        return node.is_goal
