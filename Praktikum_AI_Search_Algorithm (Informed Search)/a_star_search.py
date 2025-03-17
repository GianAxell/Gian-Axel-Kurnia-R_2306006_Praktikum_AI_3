# -*- coding: utf-8 -*-
"""A STAR SEARCH

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BCzJDReqVqn8aJmR8Y5zFOoSTmhmQRE8

A STAR SEARCH
"""

from queue import PriorityQueue

def a_star_tree_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put((0, start))
    path = {}

    while not frontier.empty():
        _, current_node = frontier.get()

        if current_node == goal:
            print("Goal node found!")
            route = reconstruct_path(path, start, goal)
            print("Optimal Route:", route)
            return True

        for neighbor, cost in graph[current_node].items():
            priority = heuristic[neighbor] + cost
            frontier.put((priority, neighbor))
            path[neighbor] = current_node

    print("Goal node not found!")
    return False

def a_star_graph_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put((0, start))
    explored = set()
    path = {}

    while not frontier.empty():
        _, current_node = frontier.get()

        if current_node == goal:
            print("Goal node found!")
            route = reconstruct_path(path, start, goal)
            print("Optimal Route:", route)
            return True

        explored.add(current_node)

        for neighbor, cost in graph[current_node].items():
            if neighbor not in explored:
                total_cost = cost + heuristic[neighbor]
                frontier.put((total_cost, neighbor))
                path[neighbor] = current_node

    print("Goal node not found!")
    return False

def reconstruct_path(path, start, goal):
    current = goal
    route = [current]
    while current != start:
        current = path[current]
        route.append(current)
    route.reverse()
    return route

# Updated heuristic values based on the image
heuristic = {
    'S': 6,
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 1,
    'G': 0
}

# Updated graph adjacency list with correct costs
graph = {
    'S': {'A': 3, 'B': 2},
    'A': {'D': 5, 'B': 1},
    'B': {'C': 2},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 1},
    'G': {}
}

# Define start and goal nodes
start_node = 'S'
goal_node = 'G'

# Run A* Tree Search
a_star_tree_search(graph, start_node, goal_node, heuristic)

# Run A* Graph Search
a_star_graph_search(graph, start_node, goal_node, heuristic)