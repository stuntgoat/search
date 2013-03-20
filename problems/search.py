

class Search(object):
    def __init__(self, tree):
        self.tree = tree

    def initial_state(self):
        """
        Returns the root node or starting state.
        """
        return self.tree.root_node

    def actions(self, node):
        """
        Returns a list of child nodes and their edge costs, if available.
        """
        return node.children

    def transition_cost(self, state, action):
        """
        Called on self.action(<choice>) and sets self.state
        to a new value.
        """
        pass

    def goal_test(self, state):
        """
        Checks self.state for the goal state.
        Returns a boolean.
        """
        raise Exception('self.goal_test has not been defined')

    def set_cost_func(self, func):
        """
        Sets the cost function.
        """
        self.cost_func = func
