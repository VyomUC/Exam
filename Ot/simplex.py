def display(equations, delta):
    print(end='\t\t')
    for i in range(len(equations[0])):  # changed to ensure flexibility with equations size
        print(equations[0][i], end='\t')
    print()
    print('Cb', end='\t')
    print('Xb', end='\t')
    
    for i in range(m): 
        print(f'x{i+1}', end='\t')
    
    for i in range(n): 
        print(f'S{i+1}', end='\t')
    
    print()

    for i in range(1, len(equations)):  # start at 1 to skip the z equation
        for coeff in equations[i]:
            print(coeff, end='\t')
        print()

    print("\nDelta values:")
    for i in range(len(delta)):
        print(delta[i], end='\t')
    print()


def getCoefficients(equation, eqno):
    coefficients = []
    
    # Add the Cb coefficient (0.0 for z, non-zero for constraints)
    if eqno != '': 
        coefficients.append(0.0)
    
    i = 0
    while i < len(equation):
        if equation[i] == '+': 
            pass
        elif equation[i] == '<=': 
            break  # to stop parsing the constraint at inequality
        elif 'x' in equation[i]:
            digit = equation[i][:equation[i].index('x')]
            if (i > 0 and equation[i-1] == '-') or equation[i][0] == '-':
                factor = -1.0
            else:
                factor = 1.0
            
            coeff = factor if digit == '' or digit == '-' else factor * float(digit)
            coefficients.append(coeff)
        elif equation[i] == '-':
            pass
        else:
            coefficients.append(float(equation[i]))
        i += 1
    
    # Add slack variables (identity matrix column)
    if eqno != '':  # only for constraints, not for z
        for i in range(n):
            identity = 1.0 if i == eqno else 0.0
            coefficients.append(identity)
    else:
        for _ in range(n): 
            coefficients.append(0.0)
    
    return coefficients


def solve(equations):
    delta = []
    for column in range(m + n):  # iterate over columns, excluding Cb and RHS
        deltaj = 0
        for row in range(1, len(equations)):  # iterate over rows excluding z
            deltaj += equations[row][0] * equations[row][column + 1]  # Cb * coefficient
        
        delta.append(deltaj - equations[0][column + 1])  # subtract z coefficients
    return delta


equations = []
m = int(input("Enter no. of variables: "))
n = int(input("Enter no. of constraints: "))

z = input("Enter objective function (z): ")
equations.append(getCoefficients(z.split(), ''))

for i in range(n):
    eq = input(f"Enter constraint {i+1}: ")
    equations.append(getCoefficients(eq.split(), i))

delta = solve(equations)
display(equations, delta)
