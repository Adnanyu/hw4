import math

Digits = 7

def f(x):
    return 4 * x**3 - 6 * x**2 - 15 * x + 2

def g(x):
    return x - f(x) / (12 * x**2 - 12 * x - 15)

p0 = 0.125
epsilon = 10**(-7)
RE = 1

n = 1
while RE >= epsilon:
    p = g(p0)
    RE = abs((p - p0) / p)
    print(n,"\t||\t",round(p0,7),"\t||\t", round(p,7),"\t||\t", RE)
    p0 = p
    n += 1

print('Approximation of the fixed point is', p)
