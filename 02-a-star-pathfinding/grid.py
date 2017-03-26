"""
grid.py: contains the classes for defining a grid layout
"""
import math


class Edge:
    def __init__(self, src_node, target_node, cost):
        self.src_node = src_node
        self.target_node = target_node
        self.cost = cost

    def __str__(self):
        return "{0} -> {1}: {2}".format(
            self.src_node,
            self.target_node,
            self.cost
        )

class Grid:
    """Holds the definition of a grid layout with some helper functions.

    Attributes:
        grid_layout: list of lists, representing a 2-dimensional grid of nodes
        edges: list of edges
    """

    def __init__(self, length, width):
        grid_row = [0] * length
        self.grid_layout = []
        for n in range(width):
            self.grid_layout.append(grid_row[:])
        self.edges = []

    def __str__(self):
        return '\n'.join(
            [' -- '.join(
                [str(x) for x in row]
            ) for row in self.grid_layout]
        )

    def is_edge(self, src, target):
        """Determines if src and target are connected by an edge in that direction."""
        for edge in self.edges:
            if edge.src_node == src and edge.target_node == target:
                return True
        return False

    def get_adjacent_nodes(self, node):
        """Returns the list of targets node points to."""
        adjacents = []
        for edge in self.edges:
            if edge.src_node == node:
                adjacents.append(edge.target_node)
        return adjacents

def node_distance(node_one, node_two):
    """
    Calculate the straight-line distance between two nodes.

    Acts as the heuristic for this implementation of A*
    """
    d_x = node_two[0] - node_one[0]
    d_y = node_two[1] - node_one[1]
    return math.sqrt(d_x * d_x + d_y*d_y)

def create_uniform_edges(grid):
    """
    Create the list of edges between every adjacent node in a square grid.
    """
    for row in range(0, len(grid.grid_layout) - 1):
        for col in range(0, len(grid.grid_layout[row])- 1):
            edge_right = Edge((row, col), (row, col+1), 1)
            edge_below = Edge((row, col), (row+1, col), 1)
            grid.edges.append(edge_right)
            grid.edges.append(edge_below)
    return grid

def find_path_a_star(grid, start, goal):
    """
    Find the shortest path between two nodes with the A* algorithm.
    """
    p_queue = [start]
    traveled_nodes = []
    g_scores = {start: 0}
    f_scores = {start: node_distance(start, goal)}
    predecessor_nodes = {}
    while len(p_queue) > 0:
        candidate = _find_min_f_score(f_scores, p_queue)
        if candidate == goal:
            return _show_path(predecessor_nodes, goal)

        p_queue.remove(candidate)
        traveled_nodes.append(candidate)
        asdf = [n for n in grid.get_adjacent_nodes(candidate) if n not in traveled_nodes]
        for adjacent in asdf:
            estimated_g_score = g_scores[candidate] + node_distance(candidate, adjacent)
            if adjacent in g_scores and estimated_g_score >= g_scores[adjacent]:
                continue

            p_queue.append(adjacent)
            predecessor_nodes[adjacent] = candidate
            g_scores[adjacent] = estimated_g_score
            f_scores[adjacent] = estimated_g_score + node_distance(adjacent, goal)
    return "No path found"

def _find_min_f_score(f_scores, node_queue):
    filtered_node_list = filter(lambda x: x in node_queue, f_scores)
    return min(filtered_node_list)

def _show_path(predecessors, target):
    path = [target]
    while target in predecessors:
        target = predecessors[target]
        path.append(target)
    return path

def grid_with_path(grid, path):
    for node in path:
        x, y = node
        grid.grid_layout[x][y] = 'X'
    print(grid)


our_grid = Grid(10, 10)
our_grid = create_uniform_edges(our_grid)
a_star_path = find_path_a_star(our_grid, (0,0), (8,7))

print(a_star_path)
print(grid_with_path(our_grid, a_star_path))
