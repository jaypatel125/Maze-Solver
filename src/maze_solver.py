# I Jay Patel, 000881881 certify that this material is my original work. No other person's work has been used without due acknowledgement. I have not made my work available to anyone else.

import heapq
from collections import deque


def maze_solver_dfs(start, is_goal, get_neighbors, maze):
    """
    Depth-First Search algorithm for solving the maze.

    Args:
    start (tuple): Starting position of the search.
    is_goal (function): Function to check if a position is the goal.
    get_neighbors (function): Function to get neighboring positions.
    maze (list): The maze grid.

    Returns:
    list: The solution path if found, otherwise None.
    """
    visited = set()
    stack = [(start, [start])]  # Stack to keep track of positions to visit, along with their paths
    while stack:
        current, path = stack.pop()  # Pop the current position and its path from the stack
        if current in visited:
            continue
        visited.add(current)  # Mark current position as visited
        if is_goal(current, maze):  # Check if current position is the goal
            return path
        for neighbor in get_neighbors(current):  # Explore neighboring positions
            stack.append((neighbor, path + [neighbor]))
    return None


def maze_solver_bfs(start, is_goal, get_neighbors, maze):
    """
    Breadth-First Search algorithm for solving the maze.

    Args:
    start (tuple): Starting position of the search.
    is_goal (function): Function to check if a position is the goal.
    get_neighbors (function): Function to get neighboring positions.
    maze (list): The maze grid.

    Returns:
    list: The solution path if found, otherwise None.
    """
    visited = set()
    queue = deque([(start, [start])])  # Queue to keep track of positions to visit, along with their paths
    while queue:
        current, path = queue.popleft()  # Pop the current position and its path from the queue
        if current in visited:
            continue
        visited.add(current)  # Mark current position as visited
        if is_goal(current, maze):  # Check if current position is the goal
            return path
        for neighbor in get_neighbors(current):  # Explore neighboring positions
            queue.append((neighbor, path + [neighbor]))
    return None


def maze_solver_astar(start, is_goal, heuristic, get_neighbors, maze):
    """
    A* Search algorithm for solving the maze.

    Args:
    start (tuple): Starting position of the search.
    is_goal (function): Function to check if a position is the goal.
    heuristic (function): Heuristic function to estimate the cost to reach the goal.
    get_neighbors (function): Function to get neighboring positions.
    maze (list): The maze grid.

    Returns:
    list: The solution path if found, otherwise None.
    """
    visited = set()
    open_list = [(heuristic(start, maze), start, [start])]  # Priority queue to keep track of positions to visit, along with their paths and estimated costs
    while open_list:
        _, current, path = heapq.heappop(open_list)  # Pop the current position, its path, and estimated cost from the priority queue
        if current in visited:
            continue
        visited.add(current)
        if is_goal(current, maze):  # Check if current position is the goal
            return path
        for neighbor in get_neighbors(current, maze):  # Explore neighboring positions
            new_path = path + [neighbor]
            g_cost = len(new_path) - 1  # Calculate the actual cost from the start to the neighbor
            f_cost = g_cost + heuristic(neighbor, maze)
            heapq.heappush(open_list, (f_cost, neighbor, new_path))  # Add the neighbor, its path, and estimated cost to the priority queue
    return None

def print_maze_with_path(maze, path):
    """
    Print the maze with the solved path indicated by '*'.

    Args:
    maze (list): The maze grid.
    path (list): The list of states representing the solved path.
    """
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if (y, x) in path:
                print('*', end='')  # Print '*' if the cell is part of the solved path
            elif maze[y][x] == 'c':
                print(' ', end='')  # Print an empty space for 'c' (clear path)
            elif maze[y][x] == 'u' or maze[y][x].isdigit():
                print(maze[y][x], end='')  # Print 'u' or digits for specified locations
            else:
                print("\u2588", end='')  # Print a block character for obstacles

        print()  # Move to the next row after printing each row
