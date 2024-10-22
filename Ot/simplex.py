import numpy as np

def initialize_simplex(c, A, b):
    """
    Initialize the simplex tableau.
    """
    num_vars = len(c)
    num_constraints = len(b)
    
    # Create the tableau
    tableau = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))
    
    # Set up the objective function in the last row
    tableau[-1, :num_vars] = -np.array(c)
    
    # Set up the constraints
    for i in range(num_constraints):
        tableau[i, :num_vars] = A[i]
        tableau[i, num_vars + i] = 1  # Slack variable
        tableau[i, -1] = b[i]  # Right-hand side
    
    return tableau

def find_pivot(tableau):
    """
    Find the pivot position.
    """
    num_rows, num_cols = tableau.shape
    col = np.argmin(tableau[-1, :-1])  # Choose entering variable (most negative coefficient)
    
    if tableau[-1, col] >= 0:
        return None  # Optimal reached if no negative coefficients in the objective function row
    
    # Ratio test to find the exiting row
    ratios = []
    for i in range(num_rows - 1):
        if tableau[i, col] > 0:
            ratios.append(tableau[i, -1] / tableau[i, col])
        else:
            ratios.append(np.inf)
    
    row = np.argmin(ratios)
    
    if ratios[row] == np.inf:
        return None  # Problem is unbounded
    
    return (row, col)

def perform_pivot(tableau, pivot):
    """
    Perform the pivot operation.
    """
    row, col = pivot
    
    # Normalize the pivot row
    tableau[row, :] /= tableau[row, col]
    
    # Eliminate all other entries in the pivot column
    for i in range(tableau.shape[0]):
        if i != row:
            tableau[i, :] -= tableau[i, col] * tableau[row, :]

def simplex(c, A, b):
    """
    Solve the linear programming problem using the simplex method.
    """
    tableau = initialize_simplex(c, A, b)
    
    while True:
        pivot = find_pivot(tableau)
        if pivot is None:
            break
        perform_pivot(tableau, pivot)
    
    return tableau[-1, -1], tableau[:-1, -1]

def input_vector(prompt, length):
    return [float(x) for x in input(prompt + f" (separate by spaces, expected {length} values): ").split()]

def main():
    num_vars = int(input("Enter the number of decision variables: "))
    num_constraints = int(input("Enter the number of constraints: "))

    print("Enter the coefficients of the objective function to maximize.")
    c = input_vector("Coefficients for the objective function", num_vars)

    A = []
    b = []
    print("Enter the coefficients for each constraint followed by the RHS value.")
    for i in range(num_constraints):
        constraint_input = input_vector(f"Constraint {i+1} coefficients and RHS", num_vars + 1)
        A.append(constraint_input[:-1])
        b.append(constraint_input[-1])

    optimal_value, variable_values = simplex(c, A, b)
    print("Optimal Value:", optimal_value)
    print("Values of Variables:", variable_values)

if __name__ == "__main__":
    main()


""""
Enter the number of decision variables: 2
Enter the number of constraints: 2
Enter the coefficients of the objective function to maximize.
Coefficients for the objective function (separate by spaces, expected 2 values): 3 5
Enter the coefficients for each constraint followed by the RHS value.
Constraint 1 coefficients and RHS (separate by spaces, expected 3 values): 1 2 18
Constraint 2 coefficients and RHS (separate by spaces, expected 3 values): 4 1 16
"""