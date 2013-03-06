"""
Utility functions for search problems and solutions.
"""

def path_from_start(current_node, parent_map):
    """
    Return a list of nodes in order from the starting node
    to the current node.
    """
    path = [current_node]
    while True:
        current_node = parent_map.get(current_node)
        if not current_node:
            break
        path.append(current_node)

    path.reverse()
    return path
