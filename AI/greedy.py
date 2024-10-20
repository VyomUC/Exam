import heapq

def greedy_best_first_search(graph, start, goal, heuristics):
    # Priority queue for managing nodes to explore; starts with the initial node
    priority_queue = [(heuristics[start], start)]
    # To keep track of visited nodes
    visited = set()
    # To track the path taken
    came_from = {start: None}

    while priority_queue:
        # Select the node with the lowest heuristic value
        current_heuristic, current_node = heapq.heappop(priority_queue)
        
        # If the goal node is reached, reconstruct the path
        if current_node == goal:
            return reconstruct_path(came_from, start, goal)
        
        # If not visited, explore the node
        if current_node not in visited:
            visited.add(current_node)
            
            # Explore each adjacent node
            for neighbor, cost in graph[current_node]:
                if neighbor not in visited:
                    # No need to recalculate the heuristic each time
                    neighbor_heuristic = heuristics[neighbor]
                    # Add to the priority queue
                    heapq.heappush(priority_queue, (neighbor_heuristic, neighbor))
                    # Record how we reached this neighbor
                    came_from[neighbor] = current_node
    
    return "Goal not reachable"

def reconstruct_path(came_from, start, goal):
    # Reconstruct the path from goal to start
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()  # Reverse the path to get it from start to goal
    return f"Goal reached: {goal}, Path: {path}"

# Example graph with heuristic values
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 6), ('E', 5)],
    'C': [('F', 9), ('G', 7)],
    'D': [],
    'E': [('G', 2), ('H', 4)],
    'F': [('I', 2)],
    'G': [('H', 1)],
    'H': [('I', 3)],
    'I': []
}

# Heuristic values estimated from each node to the goal ('I')
heuristics = {
    'A': 10, 'B': 6, 'C': 5,
    'D': 7, 'E': 3, 'F': 2,
    'G': 4, 'H': 2, 'I': 0
}

# Define the start and goal nodes
start_node = 'A'
goal_node = 'I'

# Run the greedy best-first search
result = greedy_best_first_search(graph, start_node, goal_node, heuristics)
print(result)
