import numpy as sp

# Define variable
x = sp.symbols('x')

# Define the function
f = sp.sin(x) * sp.exp(x)

# Order of derivative
n = 4

# Compute nth derivative
nth_derivative = sp.diff(f, x, n)

print("The {n}th derivative is:")
print(nth_derivative)
