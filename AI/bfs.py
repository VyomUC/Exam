class Node: 
    def __init__(self, state, parent=None): 
        self.state = state
        self.parent = parent 


class BFS: 
    def __init__(self, state_space, initial_state, goal_state): 
        self.state_space = state_space 
        self.initial_state = initial_state 
        self.goal_state = goal_state 


    def find_children(self, node): 
        children = []
        for m, n, c in self.state_space: 
            if m == node.state: 
                child_node = Node(n, node) 
                children.append(child_node) 
            elif n == node.state: 
                child_node = Node(m, node) 
                children.append(child_node) 
        return children 


    def search(self): 
        frontier = [Node(self.initial_state, None)] 
        explored = [] 
        found_goal = False 

        while frontier: 
            current_node = frontier.pop(0) 
            if current_node.state == self.goal_state: 
                found_goal = True 
                goal_node = current_node 
                break 

            children = self.find_children(current_node) 
            explored.append(current_node) 

            for child in children: 
                if child.state not in [e.state for e in explored] and child.state not in [f.state for f in frontier]: 
                    frontier.append(child) 

        if found_goal: 
            solution = [goal_node.state] 
            trace_node = goal_node 
            while trace_node.parent is not None: 
                solution.insert(0, trace_node.parent.state) 
                trace_node = trace_node.parent 
            return solution 
        else:
            return "No solution found" 


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

bfs = BFS(state_space, initial_state, goal_state)
print('Solution: ' + str(bfs.search()))