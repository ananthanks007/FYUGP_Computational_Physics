import numpy as np
import matplotlib.pyplot as plt

# Euler method - for single step

def euler(f, tn, yn, h):
	return yn + h * f(tn,yn)

# Iterating function

def solve(f, tspan, y0, h, euler):
	t = np.arange(tspan[0], tspan[1] + h, h)
	y = np.zeros(len(t))
	y[0] = y0
	
	for n in range(0, (len(t) - 1)):
		y[n+1] = euler(f, t[n], y[n], h)

	return t,y


def f(t, N):
	return -lmbda * N

tspan = [0, 1000]
h = 1
h1 = 0.1
N0 = 1000
lmbda = 0.01023
t,y = solve(f, tspan, N0, h, euler)

plt.plot(t, y)
plt.xlabel("$t$")
plt.ylabel("$N$")
plt.title("Radioactive Decay")
plt.grid(True)
plt.show()