from collections import defaultdict

# Function to add edges to the graph
def add(graph, u, v, cost):
    graph[u].append((v, cost))
    graph[v].append((u, cost))  # Since it's an undirected graph

# Graph class with heuristic support
class Graph:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic

    # A depth-limited DFS function
    def depth_limited_search(self, src, target, limit, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(src)

        if src == target:
            return True

        if limit <= 0:
            return False

        # Recur for all neighbors
        for neighbor, cost in self.graph[src]:
            if neighbor not in visited:
                if self.depth_limited_search(neighbor, target, limit - 1, visited):
                    return True

        return False

    # Iterative Deepening DFS function
    def iterative_deepening_dfs(self, src, target, max_depth):
        for depth in range(max_depth + 1):
            visited = set()
            if self.depth_limited_search(src, target, depth, visited):
                return True
        return False

# Creating the graph and heuristic
graph = defaultdict(list)
add(graph, "A", "Z", 75)
add(graph, "A", "T", 118)
add(graph, "A", "S", 140)
add(graph, "Z", "O", 71)
add(graph, "O", "S", 151)
add(graph, "T", "L", 111)
add(graph, "L", "M", 70)
add(graph, "M", "D", 75)
add(graph, "D", "C", 120)
add(graph, "S", "R", 80)
add(graph, "S", "F", 99)
add(graph, "R", "C", 146)
add(graph, "C", "P", 138)
add(graph, "R", "P", 97)
add(graph, "F", "B", 211)
add(graph, "P", "B", 101)
add(graph, "B", "G", 90)
add(graph, "B", "U", 85)
add(graph, "U", "H", 98)
add(graph, "H", "E", 86)
add(graph, "U", "V", 142)
add(graph, "V", "I", 92)
add(graph, "I", "N", 87)

heuristic = {
    "A":  366, "B": 0, "C": 160, "D": 242, "E": 161, "F": 178, "G": 77,
    "H": 151, "I": 226, "L": 244, "M": 241, "N": 234, "O": 380, "P": 98,
    "R": 193, "S": 253, "T": 329, "U": 80, "V": 199, "Z": 374
}

g = Graph(graph, heuristic)
target = "B"
max_depth = 5
src = "A"

if g.iterative_deepening_dfs(src, target, max_depth):
    print(f"Target {target} is reachable from source {src} within depth {max_depth}")
else:
    print(f"Target {target} is NOT reachable from source {src} within depth {max_depth}")