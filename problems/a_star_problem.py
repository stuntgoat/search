



class AStarProblem(object):
    def __init__(self, maze):
        self.maze = maze

    def initial_state(self):
        """
        Returns the root node or starting state.
        """
        return self.maze.start

    def actions(self, current_cost, coordinate):
        """
        Return a list of available coordinates to move next and
        their costs
        """
        return [(_n.cost, _n) for _n in node.children]

    def goal_test(self, cell_coordinates):
        """
        Returns boolean if the node is the goal.
        """
        x, y = cell_coordinates
        xx, yy = self.maze.end
        return x == xx and y == yy
