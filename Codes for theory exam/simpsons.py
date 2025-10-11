import numpy as np

# Simpsons rule for a given set of values

#### Always use Simpson's rule for even number of intervals


# Given data
x = np.array([0.25, 0.30, 0.35, 0.40, 0.45])
y = np.array([24.1, 25.5, 26.6, 27.3, 27.9])

def simpsons(x,y):
    

    # Step size (assuming equal spacing)
    h = x[1] - x[0]
    n = len(x) - 1  # number of intervals

    # Apply Simpson’s 1/3 rule
    result = (h / 3) * (y[0]+ 4 * np.sum(y[1:n:2])  + 2 * np.sum(y[2:n:2])  + y[n])

    return result

integral = simpsons(x,y)
print(f"Integral using Simpson's rule is : {integral}")

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
