class DFS:
    def __init__(self, initial_state, goal_state, state_space):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.state_space = state_space
        self.visited = set()
        self.path = []

    def find_path(self):
        self.dfs_recursive(self.initial_state)
        return self.path

    def dfs_recursive(self, current_state):
        self.visited.add(current_state)
        self.path.append(current_state)

        if current_state == self.goal_state:
            return True

        neighbors = self.get_neighbors(current_state)
        for neighbor in neighbors:
            next_state = neighbor[1]
            if next_state not in self.visited:
                if self.dfs_recursive(next_state):
                    return True
        self.path.pop()  # backtrack if no valid path found
        return False

    def get_neighbors(self, state):
        neighbors = []
        for edge in self.state_space:
            if edge[0] == state:
                neighbors.append(edge)
            elif edge[1] == state:
                neighbors.append((edge[1], edge[0], edge[2]))
        return neighbors


initial_state = "Arad"
goal_state = "Bucharest"
state_space = [
    ['Arad', 'Zerind', 75],
    ['Arad', 'Timisoara', 118],
    ['Arad', 'Sibiu', 140],
    ['Zerind', 'Oradea', 71],
    ['Timisoara', 'Lugoj', 111],
    ['Sibiu', 'Fagaras', 99],
    ['Sibiu', 'Rimnicu Vilcea', 80],
    ['Oradea', 'Sibiu', 151],
    ['Lugoj', 'Mehadia', 70],
    ['Fagaras', 'Bucharest', 211],
    ['Rimnicu Vilcea', 'Pitesti', 97],
    ['Rimnicu Vilcea', 'Craiova', 146],
    ['Mehadia', 'Drobeta', 75],
    ['Drobeta', 'Craiova', 120],
    ['Pitesti', 'Bucharest', 101],
    ['Craiova', 'Pitesti', 138],
    ['Bucharest', 'Giurgiu', 90],
    ['Bucharest', 'Urziceni', 85],
    ['Urziceni', 'Vaslui', 142],
    ['Urziceni', 'Hirsova', 98],
    ['Vaslui', 'Iasi', 92],
    ['Hirsova', 'Eforie', 86]
]

dfs_solver = DFS(initial_state, goal_state, state_space)
path = dfs_solver.find_path()

if path:
    print("Path found:")
    print(path)
else:
    print("No path found.")