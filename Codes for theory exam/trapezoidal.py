import numpy as np

# Trapezoidal Rule for given set of values


t = np.array([0,2,4,6,8,10])
v = np.array([0,6,10,14,18,20])

def trapez(t,v):
    h = t[1] - t[0]

    v_0 = v[0]
    v_n = v[-1]
    v_sum = np.sum(v[1:-1]) # sum of all middle terms

    s = (h/2) * (v_0 + 2*v_sum+ v_n)

    return s

integral = trapez(t,v)
print(integral)

# Trapezoidal Rule for given function

def f(x):
    return 5*x**2 + 2

def trapez_func(f, a, b, n):
    h = (b - a) / n
    sum = f(a) + f(b) # first and last terms

    for i in range(1, n): # middle terms
        x_i = a + i*h
        sum = sum + 2 * f(x_i)
    return (h/2) * sum

a,b,n = 0.0, 2.0, 100
integral = trapez_func(f, a, b, n)

print(integral)
    


