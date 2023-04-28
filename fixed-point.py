from math import sqrt

# Define the function g(x)
def g(x):
    return ((x**7)/5040 - (x**5)/120 + (x**3)/6 + 1/2)

# Set the initial values of prev_p and epsilon
prev_p = 0.5051
epsilon = 10**(-7)

# Set the initial value of RE to a value greater than epsilon
RE = 1.0

# Perform the fixed point iteration until RE is less than epsilon
n = 1
while RE >= epsilon:
    # Compute the next value of p
    p = g(prev_p)

    # Compute the relative error RE
    RE = abs((p - prev_p) / p)

    # Print the current iteration number, the previous value of p, the current value of p, and the current value of RE
    print(n,"\t||\t", round(prev_p,9),"\t||\t",round(p,9),"\t||\t",RE)

    # Update the value of prev_p
    prev_p = p

    # Increment the iteration counter
    n += 1

# Print the final approximation of the fixed point
print('Approximation of the fixed point is', p)