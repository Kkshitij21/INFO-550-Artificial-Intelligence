# Puzzle Solver Documentation

## Overview
The Puzzle Solver program is a Python-based implementation that solves the 8-puzzle, 15-puzzle, and 24-puzzle using search algorithms. It supports A* search with the following three heuristics:

1. **Uniform Cost Search (UCS) (H0)**
2. **Misplaced Tiles Heuristic (H1)**
3. **Manhattan Distance Heuristic (H2)**
4. **Euclidean Distance Heuristic (H3)**

---

## Features
- Supports **8-puzzle (3x3)**, **15-puzzle (4x4)**, and **24-puzzle (5x5)**.
- Provides four algorithms:
  - **Uniform Cost Search (UCS) (H0)**
  - **A* Search with Misplaced Tiles Heuristic (H1)**
  - **A* Search with Manhattan Distance Heuristic (H2)**
  - **A* Search with Euclidean Distance Heuristic (H3)**
- Tracks and displays the number of nodes expanded and the number of moves required to solve the puzzle.

---

## Classes

### 1. **puzzle8**
This class represents an 8-puzzle (3x3 grid).

**Attributes:**
- `goalState`: The 3x3 goal state for the puzzle.
- `moves`: Counter for moves taken.
- `empty`: Position of the empty tile.
- `currState`: The current state of the puzzle.

**Methods:**
- **`generateRand()`**: Generates a random 3x3 puzzle state.
- **`slide()`**: Slides a tile to a neighboring position, altering the state.
- **`print()`**: Prints the puzzle in a readable format.

### 2. **puzzle15**
This class represents a 15-puzzle (4x4 grid).

**Attributes:**
- `goalState`: The 4x4 goal state for the puzzle.
- `moves`: Counter for moves taken.
- `empty`: Position of the empty tile.
- `currState`: The current state of the puzzle.

**Methods:**
- **`generateRand()`**: Generates a random 4x4 puzzle state.
- **`slide()`**: Slides a tile to a neighboring position, altering the state.
- **`print()`**: Prints the puzzle in a readable format.

### 3. **puzzle24**
This class represents a 24-puzzle (5x5 grid).

**Attributes:**
- `goalState`: The 5x5 goal state for the puzzle.
- `moves`: Counter for moves taken.
- `empty`: Position of the empty tile.
- `currState`: The current state of the puzzle.

**Methods:**
- **`generateRand()`**: Generates a random 5x5 puzzle state.
- **`slide()`**: Slides a tile to a neighboring position, altering the state.
- **`print()`**: Prints the puzzle in a readable format.

### 4. **Node**
This class represents a search node used for the A* and UCS algorithms.

**Attributes:**
- `puzzle`: The current state of the puzzle.
- `direction`: The direction of the move that produced this node.
- `parent`: The parent node that led to this node.
- `height`: Represents the path cost for UCS.

**Methods:**
- **`fn1()`**: Calculates cost for Misplaced Tiles heuristic.
- **`fn2()`**: Calculates cost for Manhattan Distance heuristic.
- **`fn3()`**: Calculates cost for Euclidean Distance heuristic.
- **`getChildren()`**: Generates child nodes from the current node's possible moves.
- **`path()`**: Returns the path from the root node to this node.

---

## Usage

1. **Run the script**: Execute the Python script to generate and solve the puzzles.
2. **Change puzzle size**: The size can be changed to 3x3, 4x4, or 5x5 by modifying the `size` parameter in the script.
3. **Track performance**: The script logs the number of nodes expanded and the number of moves required to solve each puzzle.

---

## Results
For each heuristic, the program displays:
- **Expanded nodes**: The total number of nodes expanded.
- **Moves**: The total number of moves required to reach the goal state.


## Notes
- **Optimality**: UCS guarantees an optimal solution.
- **Heuristics**: The efficiency of A* depends on the heuristic's accuracy.
- **Performance**: Larger puzzles (like 24-puzzle) can be computationally expensive.

---

## Author
**Kkshitij Kapadia**  


