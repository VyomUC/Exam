import random

def f(x): 
    return -(x - 3)**2 + 10

def hillclimbing(start, step_size=0.01, tolerance=1e-6, max_iterations=1000):
    optima = start
    height = f(start)
    
    for _ in range(max_iterations):
        leftNeighbor = optima - step_size
        rightNeighbor = optima + step_size
        leftHeight = f(leftNeighbor)
        rightHeight = f(rightNeighbor)

        if leftHeight > height and leftHeight >= rightHeight:
            optima, height = leftNeighbor, leftHeight
        elif rightHeight > height:
            optima, height = rightNeighbor, rightHeight
        else:
            break

        # If change is smaller than tolerance, terminate
        if abs(leftHeight - height) < tolerance and abs(rightHeight - height) < tolerance:
            break
    
    return optima, height

if __name__ == "__main__":
    start = round(random.uniform(0, 10), 3)
    optima, height = hillclimbing(start)
    print(f"Starting Point: {start}")
    print(f"Local Optima: {optima}")
    print(f"f(x): {height}")