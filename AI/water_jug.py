from collections import deque

def pour(source, destination, current, volume1, volume2):
    jug1, jug2 = current
    if source == "J1":
        if jug1 > 0 and jug2 < volume2:
            amount = min(jug1, volume2 - jug2)
            return (jug1 - amount, jug2 + amount)
    else:
        if jug2 > 0 and jug1 < volume1:
            amount = min(jug2, volume1 - jug1)
            return (jug1 + amount, jug2 - amount)
    return None

def fill_jug1(volume1, current):
    return (volume1, current[1])

def fill_jug2(volume2, current):
    return (current[0], volume2)

def empty_jug1(current):
    return (0, current[1])

def empty_jug2(current):
    return (current[0], 0)

def solve(volume1, volume2, target):
    seen = set()
    queue = deque([((0, 0), [], [(0, 0)])])  # Store current, moves, and states for tracking
    while queue:
        current, moves, states = queue.popleft()  # Use BFS (queue)
        
        if current[0] == target or current[1] == target:
            return moves, states  # Return moves and water levels
        
        seen.add(current)
        possible_moves = [
            ("FJ1", fill_jug1(volume1, current)),
            ("FJ2", fill_jug2(volume2, current)),
            ("EJ1", empty_jug1(current)),
            ("EJ2", empty_jug2(current)),
            ("PJ1J2", pour("J1", "J2", current, volume1, volume2)),
            ("PJ2J1", pour("J2", "J1", current, volume1, volume2))
        ]
        
        for move, new_state in possible_moves:
            if new_state and new_state not in seen:
                queue.append((new_state, moves + [move], states + [new_state]))
    
    return None  # No solution found

volume1 = int(input("Enter volume of first jug: "))
volume2 = int(input("Enter volume of second jug: "))
target = int(input("Enter volume to be measured: "))
result = solve(volume1, volume2, target)

move_descriptions = {
    "FJ1": "Fill Jug 1",
    "FJ2": "Fill Jug 2",
    "EJ1": "Empty Jug 1",
    "EJ2": "Empty Jug 2",
    "PJ1J2": "Pour Jug 1 into Jug 2",
    "PJ2J1": "Pour Jug 2 into Jug 1"
}

if result is None:
    print("No solution exists")
else:
    moves, states = result
    print("Steps to reach the target volume:")
    for i, (move, state) in enumerate(zip(moves, states[1:]), 1):
        print(f"\n\nStep {i}: {move_descriptions[move]} \nJug 1: {state[0]}L, Jug 2: {state[1]}L")