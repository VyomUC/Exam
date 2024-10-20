import random
from collections import defaultdict

PITS = 3
SIZE = 4

class Player:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.isAlive = True
        self.hasArrow = True
        self.canMove = True
        self.killedWumpus = False

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wumpus = False
        self.pit = False
        self.gold = False
        self.stench = False
        self.breeze = False
        self.isSafe = True  # Added safety flag for optimization

class World:
    def __init__(self, size):
        self.size = size
        self.nodes = [[Node(x, y) for y in range(size)] for x in range(size)]
        self.placeElements()  # Combined placement of gold, wumpus, and pits
        self.update()

    def get_neighbors(self, x, y):
        neighbors = []
        if x > 0: neighbors.append((x-1, y))
        if x < self.size - 1: neighbors.append((x+1, y))
        if y > 0: neighbors.append((x, y-1))
        if y < self.size - 1: neighbors.append((x, y+1))
        return neighbors

    def placeElements(self):
        valid_positions = [(x, y) for x in range(self.size) for y in range(self.size) if (x, y) != (0, 0)]
        random.shuffle(valid_positions)

        # Place Gold
        x, y = valid_positions.pop()
        self.nodes[x][y].gold = True

        # Place Wumpus
        x, y = valid_positions.pop()
        self.nodes[x][y].wumpus = True

        # Place Pits
        for _ in range(PITS):
            x, y = valid_positions.pop()
            self.nodes[x][y].pit = True

    def update(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.nodes[x][y].wumpus:
                    for nx, ny in self.get_neighbors(x, y):
                        if not self.nodes[nx][ny].stench:
                            self.nodes[nx][ny].stench = True
                if self.nodes[x][y].pit:
                    for nx, ny in self.get_neighbors(x, y):
                        if not self.nodes[nx][ny].breeze:
                            self.nodes[nx][ny].breeze = True

    def display(self, player):
        horizontal_line = '-' * (self.size * 5)
        for x in range(self.size):
            print(horizontal_line)
            row = ['A' if player.position == self.nodes[x][y] else
                   'G' if self.nodes[x][y].gold else
                   'W' if self.nodes[x][y].wumpus else
                   'P' if self.nodes[x][y].pit else
                   '.' for y in range(self.size)]
            print(' | '.join(row))
        print(horizontal_line)

class KnowledgeBase:
    def __init__(self):
        self.knowledge = defaultdict(set)

    def update(self, position, info):
        self.knowledge[position].add(info)

    def remove(self, position, info):
        if info in self.knowledge[position]:
            self.knowledge[position].remove(info)

    def show(self):
        for node, info in self.knowledge.items():
            if info:
                print(node, info)

class AI:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.world = World(SIZE)
        self.player = Player(self.world.nodes[0][0], "Right")
        self.visited = {(0, 0)}
        self.steps = 0
        self.stack = []

    def getAction(self, stench, breeze, gold):
        position = self.player.position
        if gold:
            return "Grab"
        if breeze:
            self.onBreeze(position)
        if stench:
            self.onStench(position)

        possible = []
        for direction in ["Up", "Down", "Left", "Right"]:
            nextNode = self.getNewPosition(direction)
            if nextNode and self.isSafe(nextNode) and (nextNode.x, nextNode.y) not in self.visited:
                possible.append(direction)

        if possible:
            direction = random.choice(possible)
            self.stack.append((self.player.position, self.player.direction))
            return direction
        else:
            return None

    def getNewPosition(self, direction):
        position = self.player.position
        x, y = position.x, position.y
        if direction == "Right" and y != self.world.size-1: return self.world.nodes[x][y + 1]
        if direction == "Left" and y != 0: return self.world.nodes[x][y - 1]
        if direction == "Up" and x != 0: return self.world.nodes[x - 1][y]
        if direction == "Down" and x != self.world.size-1: return self.world.nodes[x + 1][y]
        return None

    def isSafe(self, position):
        # Use boolean flag instead of checking knowledge base
        return position.isSafe

    def onEmpty(self, position):
        for nx, ny in self.world.get_neighbors(position.x, position.y):
            self.kb.remove((nx, ny), "P")
            self.kb.remove((nx, ny), "W")

    def onBreeze(self, position):
        self.kb.update((position.x, position.y), "B")
        for nx, ny in self.world.get_neighbors(position.x, position.y):
            if (nx, ny) not in self.visited:
                self.kb.update((nx, ny), "P")
                self.world.nodes[nx][ny].isSafe = False

    def onStench(self, position):
        if not self.player.killedWumpus:
            self.kb.update((position.x, position.y), "S")
            for nx, ny in self.world.get_neighbors(position.x, position.y):
                if (nx, ny) not in self.visited:
                    self.kb.update((nx, ny), "W")
                    self.world.nodes[nx][ny].isSafe = False

    def move(self, direction):
        position = self.player.position
        x, y = position.x, position.y
        if direction == "Right": self.player.position = self.world.nodes[x][y + 1]
        elif direction == "Left": self.player.position = self.world.nodes[x][y - 1]
        elif direction == "Up": self.player.position = self.world.nodes[x - 1][y]
        elif direction == "Down": self.player.position = self.world.nodes[x + 1][y]
        self.visited.add((self.player.position.x, self.player.position.y))
        self.onEmpty(self.player.position)

    def killWumpus(self, position):
        for nx, ny in self.world.get_neighbors(position.x, position.y):
            if self.world.nodes[nx][ny].wumpus:
                print("Shooting Wumpus")
                self.world.nodes[nx][ny].wumpus = False
                self.player.killedWumpus = True
                self.kb.remove((nx, ny), "S")
                self.kb.remove((position.x, position.y), "S")
                self.kb.remove((position.x, position.y), "W")
                self.onEmpty(position)
                self.player.hasArrow = False

    def start(self):
        while self.player.isAlive:
            print('\n')
            print('*' * 100)
            self.steps += 1
            print(f"Step {self.steps}: ")
            self.world.display(self.player)
            stench = self.world.nodes[self.player.position.x][self.player.position.y].stench
            breeze = self.world.nodes[self.player.position.x][self.player.position.y].breeze
            gold = self.world.nodes[self.player.position.x][self.player.position.y].gold
            action = self.getAction(stench, breeze, gold)

            if action == "Grab":
                print("Player grabs Gold")
                break
            elif action:
                self.move(action)
                if self.world.nodes[self.player.position.x][self.player.position.y].wumpus:
                    self.player.isAlive = False
                    print("Player killed by Wumpus")
                elif self.world.nodes[self.player.position.x][self.player.position.y].pit:
                    self.player.isAlive = False
                    print("Player falls into Pit")
            else:
                self.killWumpus(self.player.position)
                if not self.stack:
                    print("No Possible Moves")
                    break
                previousNode, previousDirection = self.stack.pop()
                self.player.position = previousNode
                print(f"Backtracked to {(self.player.position.x, self.player.position.y)}")
        self.kb.show()

if __name__ == "__main__":
    agent = AI()
    agent.start()
