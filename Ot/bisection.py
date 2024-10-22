import sympy as sp

def bisection_method(f, a, b, tol):
    if f.subs(x, a) * f.subs(x, b) > 0:
        print("No root found in the given interval.")
        return None

    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f.subs(x, midpoint) == 0:
            return midpoint  # The midpoint is a root.
        elif f.subs(x, a) * f.subs(x, midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0

# Define the variable
x = sp.symbols('x')

# Take input from the user
expr = input("Enter the function f(x): ")

# Convert the input string into a symbolic expression
f = sp.sympify(expr)

# Input for the interval and tolerance
a = float(input("Enter the start of the interval [a]: "))
b = float(input("Enter the end of the interval [b]: "))
tolerance = float(input("Enter the tolerance: "))

# Perform the bisection method
root = bisection_method(f, a, b, tolerance)

if root is not None:
    print(f"The approximate root is: {root:.6f}")
else:
    print("Failed to find a root.")


""""
Enter the function f(x): x**2 - 4
Enter the start of the interval [a]: 1
Enter the end of the interval [b]: 5
Enter the tolerance: 0.001
"""