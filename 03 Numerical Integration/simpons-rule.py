import matplotlib.pyplot as plt
import numpy as np

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

x_vals = np.linspace(a, b, 400)
force_vals = [f(x) for x in x_vals]
plt.plot(x_vals, force_vals, label='f(x) = 5x^2+2', color='purple')
plt.fill_between(x_vals, force_vals, alpha=0.3, color='purple', label='work done area')

plt.title("WORK DONE BY VARIABLE FORCE f(x) = 5x^2+2")
plt.xlabel("DISPLACEMENT x (m)")
plt.ylabel("FORCE f(x) (N)")
plt.grid(True)
plt.legend()
plt.show()
