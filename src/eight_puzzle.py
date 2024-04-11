# I Jay Patel, 000881881 certify that this material is my original work. No other person's work has been used without due acknowledgement. I have not made my work available to anyone else.

import time
from prim_maze_generator import generate_maze, print_maze
from maze_solver import maze_solver_dfs,maze_solver_bfs, maze_solver_astar, print_maze_with_path

"""
  The Manhattan distance heuristic is suitable for maze-solving problems because:

    1. - It is a single approach that is consistent and its working is based on the admissible part of it that can never overestimate the cost to reach the goal.
       - This properties as a part of this heuristics offer a guarantee to always get an optimal solution for this algorithm.

    2. - Where navigation follows the limited directions of horizontal and vertical movements in mazes,
       - the hypotenuse in the distance matrix is made equivalent to the length of shortest way between two points.
       - This reason is that, in case of a grid based maze cells adjacent along rows and columns possess the monopoly of movement, are blocked from direct entry and only limited pathways are available.
       - one is located at the center of the search space and the other randomly selects a location within a certain distance to the center, which is called the Manhattan distance and calculates the shortest path between these adjacent cells.

    3. - The computation of Manhattan distance is simple, fast, and straightforward - only arithmetic operations are needed to calculate it.
       - It is summed by each difference to the absolute value in the x-axis and then y-axis for the current point.
       - and by preserving the mathematics and physics at their core while optimizing performance in terms of accuracy and computational efficiency, it offers real-time gaming-like experience.
"""

def is_goal(state, maze):
    """
    Check if a given state is a goal state.

    Args:
    state (tuple): The current state.
    maze (list): The maze grid.

    Returns:
    bool: True if the state is a goal state, False otherwise.
    """
    y, x = state
    return y == len(maze) - 1 and maze[y][x] == 'c'


def next_states(state, maze):
    """
    Generate next possible states from a given state.

    Args:
    state (tuple): The current state.
    maze (list): The maze grid.

    Returns:
    list: List of next possible states from the current state.
    """
    height = len(maze)
    width = len(maze[0])
    y, x = state

    possible_states = []  # List to store possible next states
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dy, dx in moves:
        new_y, new_x = y + dy, x + dx
        if 0 <= new_y < height and 0 <= new_x < width and maze[new_y][new_x] != 'w':
            possible_states.append((new_y, new_x))  # Add valid next state to the list

    return possible_states


def heuristic(state, maze):
    """
    Heuristic function to estimate the cost to reach the goal from a given state using Manhattan distance.

    Args:
    state (tuple): The current state.
    maze (list): The maze grid.

    Returns:
    float: The estimated cost to reach the goal from the current state.
    """
    goal_y = len(maze) - 1
    goal_x = len(maze[0]) // 2
    y, x = state  # Current state's coordinates
    return abs(goal_y - y) + abs(goal_x - x)  # Manhattan distance


def solve_maze_dfs(maze):
    """
    Solve the maze using Depth-First Search algorithm.

    Args:
    maze (list): The maze grid.

    Returns:
    tuple: A tuple containing the solution path and the time taken for solving.
    """
    start_time = time.time()  # Record starting time
    start_state = (0, maze[0].index('c'))
    path = maze_solver_dfs(start_state, is_goal, lambda s: next_states(s, maze), maze)  # Solve maze using DFS
    end_time = time.time()  # Record ending time
    return path, end_time - start_time  # Return solution path and time taken


def solve_maze_bfs(maze):
    """
    Solve the maze using Breadth-First Search algorithm.

    Args:
    maze (list): The maze grid.

    Returns:
    tuple: A tuple containing the solution path and the time taken for solving.
    """
    start_time = time.time()  # Record starting time
    start_state = (0, maze[0].index('c'))
    path = maze_solver_bfs(start_state, is_goal, lambda s: next_states(s, maze), maze)  # Solve maze using BFS
    end_time = time.time()  # Record ending time
    return path, end_time - start_time  # Return solution path and time taken


def solve_maze_astar(maze):
    """
    Solve the maze using A* Search algorithm.

    Args:
    maze (list): The maze grid.

    Returns:
    tuple: A tuple containing the solution path and the time taken for solving.
    """
    start_time = time.time()  # Record starting time
    start_state = (0, maze[0].index('c'))
    path = maze_solver_astar(start_state, is_goal, heuristic, lambda state, maze: next_states(state, maze), maze)
    end_time = time.time()  # Record ending time
    return path, end_time - start_time  # Return solution path and time taken


def get_start_state(maze):
    """
    Get the starting state of the maze.

    Args:
    maze (list): The maze grid.

    Returns:
    tuple: The starting state coordinates.
    """
    start_position = (0, maze[0].index('c'))  # Assuming 'c' represents the starting position
    return start_position  # Return starting state


if __name__ == "__main__":
    height = int(input("Maze Height: "))
    width = int(input("Maze Width: "))
    difficulty = float(input("Difficulty (0.0 -> 1.0): "))

    maze = generate_maze(height, width, True, difficulty)
    print("Original Maze:")
    print_maze(maze)  # Print original maze

    start_state = get_start_state(maze)  # Get starting state

    print("\nSolving maze using Depth-First Search:")
    dfs_path, dfs_time = solve_maze_dfs(maze)
    dfs_path_length = len(dfs_path) - 1 if dfs_path else 0  # Calculate path length
    print("Solution Path Length:", dfs_path_length)
    print("Time taken:", dfs_time, "seconds")
    print_maze_with_path(maze, dfs_path)  # Print maze with solution path

    print("\nSolving maze using Breadth-First Search:")
    bfs_path, bfs_time = solve_maze_bfs(maze)
    bfs_path_length = len(bfs_path) - 1 if bfs_path else 0  # Calculate path length
    print("Solution Path Length:", bfs_path_length)
    print("Time taken:", bfs_time, "seconds")
    print_maze_with_path(maze, bfs_path)  # Print maze with solution path

    print("\nSolving maze using A* Search:")
    astar_path, astar_time = solve_maze_astar(maze)
    astar_path_length = len(astar_path) - 1 if astar_path else 0  # Calculate path length
    print("Solution Path Length:", astar_path_length)
    print("Time taken:", astar_time, "seconds")
    print_maze_with_path(maze, astar_path)  # Print maze with solution path

