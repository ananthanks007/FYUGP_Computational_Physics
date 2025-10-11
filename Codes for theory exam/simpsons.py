import numpy as np

# Simpsons rule for a given set of values




# Simpson's Rule for given function

def f(x):
    return 5*x**2 + 2

def simpson_work(f, a, b, n):
    h = (b - a) / n
    result = f(a)
    for i in range(1, n, 2):
        result = result + 4 * f(a + i * h)
    for i in range(2, n, 2):
        result = result + 2 * f(a + i * h)
    result += f(b)
    return (h / 3) * result

a, b, n = 0.0, 2.0, 100
work = simpson_work(f, a, b, n)

print(f"work done by force f(x) = 5x^2+2 from x = {a} to x = {b} is : {work:.6f} J")
