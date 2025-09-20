import numpy as np
import matplotlib.pyplot as plt

def lin_reg(x, y):
     sum_x = np.sum(x)
     sum_y = np.sum(y)
     sum_xy = np.sum(x * y)
     sum_x2 = np.sum(x * x)
     n = len(x)
     m = ((n * sum_xy) - sum_x * sum_y)/((n * sum_x2) - (sum_x)**2)
     b = (sum_y - m * sum_x)/n
     return m,b
x = np.array([1, 2 , 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([193.12, 195.87, 197.14,196.45, 195.10, 198.23,196.89,200.54,201.76,203.12 ])
m,b = lin_reg(x,y)
print(f" Slope : m = {m} , and intercept: b = {b}")

plt.scatter(x, y, color = 'blue', label = "real data points")
plt.xlabel("Day")
plt.ylabel("Closing Price (in USD)")

print(f"Equation of the line : y = {m} * x_fit + {b}")

plt.plot(x, m * x + b , color = 'red', label ='least square fit')
plt.title("Apple (AAPL) Stock Price data set (June 2024)")
plt.legend()
plt.grid(True)
plt.show()