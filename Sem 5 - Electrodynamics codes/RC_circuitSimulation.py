import numpy as np
import matplotlib.pyplot as plt

# Parameters
R = 1000            # Resistance (ohm)
C = 100e-6          # Capacitance (F)
Q0 = 1e-3           # Maximum charge (C)

# Time array
t = np.linspace(0, 5, 1000)

# -------- Combined DC Graph --------

Q_growth = Q0 * (1 - np.exp(-t/(R*C)))

Q_decay = Q0 * np.exp(-t/(R*C))

plt.figure(figsize=(8,5))

# plt.xlim(0, 0.5) # limiting the x-axis to show the decay properly
plt.plot(t, Q_growth, label='Growth of Charge')

plt.plot(t, Q_decay, label='Decay of Charge')

plt.xlabel('Time (s)')
plt.ylabel('Charge (C)')
plt.title('Growth and Decay of Charge in DC RC Circuit')

plt.legend()

plt.grid(True)

plt.show()


# -------- AC Graph --------

f = 2                      # Frequency (Hz)

omega = 2 * np.pi * f

t_ac = np.linspace(0, 5, 2000)

Q_ac = Q0 * np.abs(np.sin(omega * t_ac))

plt.figure(figsize=(8,5))

plt.plot(t_ac, Q_ac)

plt.xlabel('Time (s)')
plt.ylabel('Charge (C)')
plt.title('Charge Variation in AC RC Circuit')

plt.grid(True)

plt.show()