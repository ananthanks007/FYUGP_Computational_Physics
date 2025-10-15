import numpy as np
import matplotlib.pyplot as plt

# Initial conditions and constants
x0 = 5          # initial amplitude
w0 = 2 * np.pi  # natural angular frequency
m = 2           # mass
b = 0.5         # damping coefficient (controls rate of decay)

# Time range
t = np.linspace(0, 5, num=1000)

# Damped angular frequency
wd = np.sqrt(w0**2 - (b/(2*m))**2)

# Position and momentum as functions of time
x_t = x0 * np.exp(-b*t/(2*m)) * np.sin(wd*t)
p_t = m * (np.exp(-b*t/(2*m)) * (wd*np.cos(wd*t) - (b/(2*m))*np.sin(wd*t))) * x0

# Plot configuration and phase space
plt.figure(figsize=(8,15))

# Configuration space plot
plt.subplot(2,1,1)
plt.plot(t, x_t)
plt.xlabel('Time')
plt.ylabel('Position')
plt.grid(True)
plt.title('Configuration Space (Damped Oscillator)')

# Phase space plot
plt.subplot(2,1,2)
plt.plot(x_t, p_t)
plt.xlabel('Position')
plt.ylabel('Momentum')
plt.title('Phase Space (Damped Oscillator)')
plt.grid(True)

plt.show()
