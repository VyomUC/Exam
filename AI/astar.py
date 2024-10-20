from queue import PriorityQueue
from collections import defaultdict

def a_star(graph, start, heuristic, goal="B"):
    
    # Initialize priority queue with the start node and its heuristic value
    fringe = PriorityQueue()
    fringe.put((heuristic[start], [start, 0]))  # (priority, [node, traveled_distance])
    
    path = []  # List to store the final path
    total_distance = 0  # Track the total distance from the start
    
    while not fringe.empty():
        # Get the node with the lowest f value (heuristic + traveled distance)
        current_node, traveled = fringe.get()[1]
        
        # Add current node to the path and update total distance traveled
        path.append(current_node)
        total_distance += traveled
        
        # Check if the current node is the goal
        if current_node == goal:
            return path
        
        # Explore neighbors of the current node
        for neighbor, gn in graph[current_node]:
            # Only add neighbors that haven't been visited (not in the current path)
            if neighbor not in path:
                # Calculate total priority: heuristic + actual distance traveled + distance to neighbor
                priority = heuristic[neighbor] + gn + total_distance
                fringe.put((priority, [neighbor, gn]))
    
    return []  # Return empty list if no path is found

def add_edge(graph, u, v, cost):
    #Add an edge between two nodes in the graph.
    graph[u].append((v, cost))
    graph[v].append((u, cost))  # Undirected graph, so add edge in both directions

# Initialize the graph and add edges between nodes
graph = defaultdict(list)

edges = [
    ("A", "Z", 75), ("A", "T", 118), ("A", "S", 140), ("Z", "O", 71), ("O", "S", 151), 
    ("T", "L", 111), ("L", "M", 70), ("M", "D", 75), ("D", "C", 120), ("S", "R", 80), 
    ("S", "F", 99), ("R", "C", 146), ("C", "P", 138), ("R", "P", 97), ("F", "B", 211), 
    ("P", "B", 101), ("B", "G", 90), ("B", "U", 85), ("U", "H", 98), ("H", "E", 86), 
    ("U", "V", 142), ("V", "I", 92), ("I", "N", 87)
]

for u, v, cost in edges:
    add_edge(graph, u, v, cost)

# Heuristic estimates (straight-line distances to goal B)
heuristic = {
    "A": 366, "B": 0, "C": 160, "D": 242, "E": 161, "F": 178, "G": 77,
    "H": 151, "I": 226, "L": 244, "M": 241, "N": 234, "O": 380, "P": 98,
    "R": 193, "S": 253, "T": 329, "U": 80, "V": 199, "Z": 374
}

# Get user input for the starting node
start = input("Enter start node: ")

# Perform A* search and print the result
path = a_star(graph, start, heuristic)

if path:
    print("Path found:", path)
else:
    print("No path found")