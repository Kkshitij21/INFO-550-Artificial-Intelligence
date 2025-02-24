import heapq
import random
import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, position, cost=0, parent=None):
        self.position = position
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost


def get_neighbors(position, grid):
    neighbors = []
    x, y = position
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        new = (x + dx, y + dy)
        if 0 <= new[0] < len(grid) and 0 <= new[1] < len(grid[0]) and grid[new[0]][new[1]] == 0:
            neighbors.append(new)
    return neighbors


def get_neighbors_diagonal(position, grid):
    neighbors = []
    x, y = position
    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]
    for dx, dy in directions:
        new = (x + dx, y + dy)
        if 0 <= new[0] < len(grid) and 0 <= new[1] < len(grid[0]) and grid[new[0]][new[1]] == 0:
            neighbors.append(new)
    return neighbors


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def heuristic_diagonal(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


# Uniform Cost Search (UCS)
def uniform_cost_search(start, goal, grid, dist_func):
    start_node = Node(start)
    goal_node = Node(goal)

    open_list = []
    closed_set = set()
    expanded_nodes = 0

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        expanded_nodes += 1

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1], expanded_nodes

        closed_set.add(current_node.position)

        for neighbor in dist_func(current_node.position, grid):
            if neighbor in closed_set:
                continue

            neighbor_node = Node(neighbor, current_node.cost + 1, current_node)
            heapq.heappush(open_list, neighbor_node)

    return None, expanded_nodes


# Greedy Best First Search
def greedy(start, goal, grid, dist_func, heur_func):
    start_node = Node(start)
    goal_node = Node(goal)

    open_list = []
    closed_set = set()
    expanded_nodes = 0

    heapq.heappush(open_list, (heur_func(start, goal), start_node))

    while open_list:
        _, current_node = heapq.heappop(open_list)
        expanded_nodes += 1

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1], expanded_nodes

        closed_set.add(current_node.position)

        for neighbor in dist_func(current_node.position, grid):
            if neighbor in closed_set:
                continue

            neighbor_node = Node(neighbor, 0, current_node)
            heapq.heappush(open_list, (heur_func(neighbor, goal), neighbor_node))

    return None, expanded_nodes


# A* Search
def a_star(start, goal, grid, dist_func, heur_func):
    start_node = Node(start)
    goal_node = Node(goal)

    open_list = []
    closed_set = set()
    expanded_nodes = 0

    heapq.heappush(open_list, (0, start_node))

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)
        expanded_nodes += 1

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1], expanded_nodes

        closed_set.add(current_node.position)

        for neighbor in dist_func(current_node.position, grid):
            if neighbor in closed_set:
                continue

            new_cost = current_node.cost + 1
            neighbor_node = Node(neighbor, new_cost, current_node)
            total_cost = new_cost + heur_func(neighbor, goal)
            heapq.heappush(open_list, (total_cost, neighbor_node))

    return None, expanded_nodes


def pacman_viz(grid, path, start, goal, algo_name, expanded_nodes):
    grid_array = np.array(grid)
    fig, ax = plt.subplots()

    cmap = plt.cm.get_cmap('gray')
    ax.imshow(grid_array, cmap=cmap, interpolation='none')

    ax.plot(start[1], start[0], 'go', markersize=10, label="Start")
    ax.plot(goal[1], goal[0], 'ro', markersize=10, label="Goal")

    if path:
        for position in path[1:-1]:
            ax.plot(position[1], position[0], 's', color='lime', markersize=8)

    ax.legend(loc='upper right')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"{algo_name}\nExpanded Nodes: {expanded_nodes}, Moves: {len(path) if path else 0}")
    plt.show()


def generate_random_grid(size=10, obstacle_probability=0.3):
    grid = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if (i, j) not in [(0, 0), (size-1, size-1)] and random.random() < obstacle_probability:
                grid[i][j] = 1

    start = (0, 0)
    goal = (size-1, size-1)
    return grid, start, goal


# Generate the grid
grid, start, goal = generate_random_grid(10)

# Uniform Cost Search
ucs_path, ucs_expanded = uniform_cost_search(start, goal, grid, get_neighbors_diagonal)
pacman_viz(grid, ucs_path, start, goal, "Uniform Cost Search", ucs_expanded)

# Greedy Best-First Search
greedy_path, greedy_expanded = greedy(start, goal, grid, get_neighbors_diagonal, heuristic_diagonal)
pacman_viz(grid, greedy_path, start, goal, "Greedy Best First Search", greedy_expanded)

# A* Search
a_star_path, a_star_expanded = a_star(start, goal, grid, get_neighbors_diagonal, heuristic_diagonal)
pacman_viz(grid, a_star_path, start, goal, "A* Search", a_star_expanded)
