import math

DEGREE = 5
TOLERANCE = 1e-6  # A small tolerance for the stopping condition in bisection

def display(coeffs):
    print('f(x) = ', end='')
    for i in range(DEGREE, -1, -1):
        current = coeffs[DEGREE-i]
        if math.trunc(current) == int(current):
            current = int(current)
        if current > 0: 
            sign = '+' if i != DEGREE else ''  # No plus sign for the first term
        elif current < 0:
            sign = '-'  # Minus sign for negative coefficients
        else:
            continue  # Skip zero coefficients
        
        current = '' if abs(current) == 1 and i != 0 else abs(current)
        if i == 0:  # No x^0 term
            print(f'{sign} {current}')
        else:
            print(f'{sign} {current}x^{i}', end=' ')

def f(x):
    result = 0
    for i in range(DEGREE + 1):
        result += coeffs[i] * (x ** (DEGREE - i))
    return result

def getInterval(initial=1):
    last_sign = -1 if f(initial - 1) < 0 else 1
    for i in range(initial, initial + 100):
        current_f = f(i)
        current_sign = -1 if current_f < 0 else 1
        if last_sign == -1 and current_sign == 1:
            return i - 1, i, '-+'
        if last_sign == 1 and current_sign == -1:
            return i - 1, i, '+-'
        last_sign = current_sign
    raise ValueError("No interval found with opposite signs.")

def bisection():
    lower, upper, signs = getInterval()
    while True:
        xi = (lower + upper) / 2
        answer = f(xi)
        if abs(answer) < TOLERANCE:
            return xi
        if signs == '-+':
            if answer < 0:
                lower = xi
            else:
                upper = xi
        else:
            if answer > 0:
                lower = xi
            else:
                upper = xi

coeffs = []
for power in range(DEGREE, -1, -1):
    while True:
        try:
            coeff = float(input(f"Enter coefficient of x^{power}: "))
            coeffs.append(coeff)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

display(coeffs)

try:
    root = bisection()
    print(f'Root: {root}')
except ValueError as e:
    print(e)
