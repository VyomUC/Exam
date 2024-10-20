from collections import deque

class WumpusWorld:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.world = [['' for _ in range(grid_size)] for _ in range(grid_size)]
        self.agent_position = (0, 0)
        self.visited = set()
        self.safe_positions = set([(0, 0)])

    def add_wumpus(self, position):
        self.world[position[0]][position[1]] = 'W'

    def add_pit(self, position):
        self.world[position[0]][position[1]] = 'P'

    def add_gold(self, position):
        self.world[position[0]][position[1]] = 'G'

    def move_agent(self, position):
        self.agent_position = position
        self.visited.add(position)

    def get_neighbors(self, position):
        neighbors = []
        x, y = position
        if x > 0:
            neighbors.append((x - 1, y))
        if x < self.grid_size - 1:
            neighbors.append((x + 1, y))
        if y > 0:
            neighbors.append((x, y - 1))
        if y < self.grid_size - 1:
            neighbors.append((x, y + 1))
        return neighbors

    def is_safe(self, position):
        return position in self.safe_positions

    def update_safe_positions(self, position):
        self.safe_positions.update([neighbor for neighbor in self.get_neighbors(position) if self.world[neighbor[0]][neighbor[1]] == ''])

    def check_current_position(self):
        position_type = {'G': 'GOLD_FOUND', 'W': 'WUMPUS', 'P': 'PIT'}
        return position_type.get(self.world[self.agent_position[0]][self.agent_position[1]], 'SAFE')

# Initialize Wumpus World
wumpus_world = WumpusWorld(grid_size=4)
wumpus_world.add_wumpus((1, 2))
wumpus_world.add_pit((2, 1))
wumpus_world.add_pit((3, 3))
wumpus_world.add_gold((3, 0))

# Interactive loop for the user to find the gold
def play_game(wumpus_world):
    print("Welcome to Wumpus World!")
    print("Your goal is to find the gold.")
    print("You can move using 'up', 'down', 'left', or 'right'. Type 'quit' to exit.\n")
    
    move_map = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    while True:
        print(f"Current Position: {wumpus_world.agent_position}")
        move = input("Enter your move: ").strip().lower()

        if move == "quit":
            print("Exiting game. Goodbye!")
            break

        if move in move_map:
            dx, dy = move_map[move]
            new_position = (wumpus_world.agent_position[0] + dx, wumpus_world.agent_position[1] + dy)
        else:
            print("Invalid move. Please enter 'up', 'down', 'left', or 'right'.")
            continue

        if new_position in wumpus_world.get_neighbors(wumpus_world.agent_position):
            wumpus_world.move_agent(new_position)
            status = wumpus_world.check_current_position()
            if status == "GOLD_FOUND":
                print("Congratulations! You found the gold!")
                break
            elif status == "WUMPUS":
                print("Oh no! You encountered the Wumpus! Game over.")
                break
            elif status == "PIT":
                print("Oh no! You fell into a pit! Game over.")
                break
            else:
                wumpus_world.update_safe_positions(new_position)
                print("Safe move. Keep going!")
        else:
            print("Invalid move. Out of bounds or not a valid neighbor.")

play_game(wumpus_world)
