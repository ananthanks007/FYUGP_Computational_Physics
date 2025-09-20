import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 5*x**2 + 2

def trapez(f, a, b, n):
    h = (b - a) / n
    sum = 0
    x = 0.5 * h
    for i in range(1, n):
        sum = sum + h * f(x)
        x = x + h
    return sum

a, b, n = 0.0, 2.0, 1000
work = trapez(f, a, b, n)

print(f"work done by f(x) = 5x^2+2 from x = {a} to x = {b} is : {work:.6f} J")

x_val = np.linspace(a, b, 400)
force_val = [f(x) for x in x_val]
plt.plot(x_val, force_val, label='f(x) = 5x^2+2', color='darkorange')

n = 20
h = (b - a) / n
for i in range(n):
    x0 = a + i * h
    x1 = x0 + h
    plt.fill([x0, x0, x1, x1], [0, f(x0), f(x1), 0], 'orange', edgecolor='black', alpha=0.4)

plt.title('WORK DONE BY VARIABLE FORCE USING TRAPEZOIDAL RULE')
plt.xlabel('DISPLACEMENT x (m)')
plt.ylabel('FORCE f(x) (N)')
plt.grid(True)
plt.legend()
plt.show()
