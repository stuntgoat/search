from search import Search


class AStarProblem(Search):
    def __init__(self, maze):
        self.maze = maze

    def initial_state(self):
        """
        Returns the root node or starting state.
        """
        return 0, self.maze.start

    def actions(self, coordinates):
        """
        Return a list of available coordinates to move next and
        their costs
        """
        return [(1, x) for x in self.maze.available_moves(coordinates)]

    def goal_test(self, cell_coordinates):
        """
        Returns boolean if the node is the goal.
        """
        x, y = cell_coordinates
        xx, yy = self.maze.end
        return x == xx and y == yy
