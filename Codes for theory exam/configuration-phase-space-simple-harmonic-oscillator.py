import numpy as np
import matplotlib.pyplot as plt

x0 = 5
w = 2*np.pi
m = 2

t= np.linspace(0,2*np.pi, num=1000)


x_t = x0*np.sin(w*t)
p_t = m*x0*w*np.cos(w*t)


plt.figure(figsize=(8,15))
plt.subplot(2,1,1)
plt.plot(t,x_t)
plt.xlabel('Time')
plt.ylabel('Position')
plt.grid(True)
plt.title('Configuration Space')

plt.subplot(2,1,2)
plt.plot(x_t,p_t)
plt.xlabel('Position')
plt.ylabel('Momentum')
plt.title('Phase Space')
plt.grid(True)
plt.show()