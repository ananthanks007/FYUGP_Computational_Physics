import numpy as np
import matplotlib.pyplot as plt

# Circuit parameters
R = 10
L = 0.5
V = 5

# Time
t = np.linspace(0,1,1000)

# Time constant
tau = L/R

# DC response
I_dc = (V/R)*(1-np.exp(-t/tau))


# AC parameters
f = 5
omega = 2*np.pi*f

# Inductive reactance
X_L = omega*L

# Impedance
Z = np.sqrt(R**2 + X_L**2)

# AC current
I_ac = (V/Z)*np.sin(omega*t-np.arctan(X_L/R))

# AC voltage
V_ac = V*np.sin(omega*t)


# DC graph
plt.plot(t,I_dc)
plt.xlabel("Time")
plt.ylabel("Current")
plt.title("RL Circuit Response under DC")
plt.grid()
plt.show()


# AC graph
plt.plot(t,V_ac,label="Voltage")
plt.plot(t,I_ac,label="Current")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("RL Circuit Response under AC")
plt.legend()
plt.grid()
plt.show()