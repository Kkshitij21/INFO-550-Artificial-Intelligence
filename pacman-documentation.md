# Pathfinding Algorithm Documentation

## Overview
This script implements and visualizes three pathfinding algorithms to navigate a grid from a start to a goal position. The algorithms are:

1. **Uniform Cost Search (UCS)**
2. **Greedy Best-First Search**
3. **A* Search**

The script generates a random grid with obstacles, visualizes the path, and reports the number of expanded nodes and moves for each algorithm.

---

## Features
- **Random Grid Generation**: Generates a nxn grid with random obstacles.
- **Pathfinding Algorithms**: Implements UCS, Greedy Best-First Search, and A* Search.
- **Visualization**: Uses Matplotlib to visualize the path, start, goal, and expanded nodes.
- **Performance Metrics**: Reports the number of expanded nodes and moves for each algorithm.

---

## Classes

### **Node**
Represents a node in the search space.

**Attributes:**
- `position` (tuple): The (x, y) position of the node.
- `cost` (int): The cost to reach this node.
- `parent` (Node): Reference to the parent node.

**Methods:**
- **`__lt__`**: Compares nodes by cost for priority queue ordering.

---

## Functions

### **get_neighbors(position, grid)**
Finds adjacent neighbors (up, down, left, right) for a given position on the grid.

### **get_neighbors_diagonal(position, grid)**
Finds adjacent and diagonal neighbors for a given position on the grid.

### **heuristic(a, b)**
Calculates the Manhattan distance between two points `a` and `b`.

### **heuristic_diagonal(a, b)**
Calculates the Chebyshev distance between two points `a` and `b`, allowing for diagonal movement.

### **uniform_cost_search(start, goal, grid, dist_func)**
Implements Uniform Cost Search to find the shortest path.

**Parameters:**
- `start` (tuple): Starting position.
- `goal` (tuple): Goal position.
- `grid` (list): 2D grid.
- `dist_func` (function): Neighbor function (e.g., `get_neighbors_diagonal`).

**Returns:**
- `path` (list): List of positions forming the path.
- `expanded_nodes` (int): Total nodes expanded.

### **greedy(start, goal, grid, dist_func, heur_func)**
Implements Greedy Best-First Search.

**Parameters:**
- `start` (tuple): Starting position.
- `goal` (tuple): Goal position.
- `grid` (list): 2D grid.
- `dist_func` (function): Neighbor function.
- `heur_func` (function): Heuristic function.

**Returns:**
- `path` (list): List of positions forming the path.
- `expanded_nodes` (int): Total nodes expanded.

### **a_star(start, goal, grid, dist_func, heur_func)**
Implements A* Search to find the optimal path.

**Parameters:**
- `start` (tuple): Starting position.
- `goal` (tuple): Goal position.
- `grid` (list): 2D grid.
- `dist_func` (function): Neighbor function.
- `heur_func` (function): Heuristic function.

**Returns:**
- `path` (list): List of positions forming the path.
- `expanded_nodes` (int): Total nodes expanded.

### **pacman_viz(grid, path, start, goal, algo_name, expanded_nodes)**
Visualizes the path taken by a search algorithm.

**Parameters:**
- `grid` (list): 2D grid.
- `path` (list): The path from start to goal.
- `start` (tuple): Start position.
- `goal` (tuple): Goal position.
- `algo_name` (str): Name of the algorithm.
- `expanded_nodes` (int): Number of nodes expanded.

### **generate_random_grid(size=10, obstacle_probability=0.3)**
Generates a random 10x10 grid with obstacles.

**Parameters:**
- `size` (int): Size of the grid.
- `obstacle_probability` (float): Probability of placing an obstacle at each cell.

**Returns:**
- `grid` (list): The generated 2D grid.
- `start` (tuple): Start position.
- `goal` (tuple): Goal position.

---

## Usage

1. **Generate the Grid**
   ```python
   grid, start, goal = generate_random_grid(10)
   ```

2. **Run the Algorithms**
   ```python
   ucs_path, ucs_expanded = uniform_cost_search(start, goal, grid, get_neighbors_diagonal)
   greedy_path, greedy_expanded = greedy(start, goal, grid, get_neighbors_diagonal, heuristic_diagonal)
   a_star_path, a_star_expanded = a_star(start, goal, grid, get_neighbors_diagonal, heuristic_diagonal)
   ```

3. **Visualize the Results**
   ```python
   pacman_viz(grid, ucs_path, start, goal, "Uniform Cost Search", ucs_expanded)
   pacman_viz(grid, greedy_path, start, goal, "Greedy Best First Search", greedy_expanded)
   pacman_viz(grid, a_star_path, start, goal, "A* Search", a_star_expanded)
   ```

---

## Notes
- **Visualization**: Paths and expanded nodes are visualized in the grid.
- **Optimality**: A* guarantees optimality with an admissible heuristic.
- **Performance**: Greedy is faster but not guaranteed to be optimal.

---

## Author
**Author**: Kkshitij Kapadia 

---


