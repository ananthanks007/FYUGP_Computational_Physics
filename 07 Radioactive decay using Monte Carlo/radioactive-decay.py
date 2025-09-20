import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# Define the Monte Carlo simulation function
def monte_carlo_decay_simulation(n0, lmbda, steps):
    decay_mc = np.zeros(steps)  # to store N at each step
    n = n0                      # current number of particles
    t_half_mc = None            # simulated half-life (step count)

    for t in range(steps):
        decay_mc[t] = n
        decayd = np.sum(np.random.rand(n) < lmbda)  # count decayed particles
        n = n - decayd

        if t_half_mc is None and n < n0 / 2:
            t_half_mc = t

    return decay_mc, t_half_mc

# Parameters
n0 = 1000
lmbda = 0.01023          # decay constant
'''
decay constant of N-13 = 0.06966
decay constant of Ga-68 = 0.01023
'''
steps = 1000              # number of simulation steps

# Run the Monte Carlo simulation
decay_mc, t_half_mc = monte_carlo_decay_simulation(n0, lmbda, steps)

# Analytical solution for comparison
t_half = np.log(2) / lmbda  # theoretical half-life
time_array = np.arange(steps)
decay_analytical = n0 * np.exp(-lmbda * time_array)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time_array, decay_mc, label='Monte Carlo Simulation', color='blue', marker='o', markersize=3)
plt.plot(time_array, decay_analytical, label='Analytical Solution', color='red', linestyle='--')
plt.xlabel('Time Steps')
plt.ylabel('Number of Particles')
plt.title('Monte Carlo Simulation of Radioactive Decay')
# plt.xlim(0,300) # To make the graph neater in case if the t-half is small
plt.grid(True)
plt.legend()
plt.show()

print("Simulated Half-life: ", t_half_mc)
print("Theoretical Half-life :", t_half)