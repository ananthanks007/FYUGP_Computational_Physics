import numpy as np
import matplotlib.pyplot as plt

# === Euler Method Definition ===
def euler(x, y, fxy, h):
    return y + h * fxy(x, y)

# === Constants and Initial Conditions ===
g = 9.81  # acceleration due to gravity (m/s^2)
dt = 0.01  # time step
v0 = 50  # initial speed (m/s)
theta = 45  # launch angle (degrees)
theta_rad = np.radians(theta)

vx0 = v0 * np.cos(theta_rad)
vy0 = v0 * np.sin(theta_rad)

# === Theoretical Calculations (No Air Resistance) ===
R_theory = (v0**2 * np.sin(2 * theta_rad)) / g  # Range
H_theory = (v0**2 * (np.sin(theta_rad))**2) / (2 * g) # Maximum Height
T_theory = (2 * v0 * np.sin(theta_rad)) / g  # Time of Flight

# Initial state
x, y = 0, 0
vx, vy = vx0, vy0
t = 0

X, Y, T = [], [], []

# === Projectile Motion without Air Resistance ===
while y >= 0:
    X.append(x)
    Y.append(y)
    T.append(t)

    # Euler updates
    x = euler(t, x, lambda t, x: vx, dt)
    y = euler(t, y, lambda t, y: vy, dt)
    vx = euler(t, vx, lambda t, vx: 0, dt)
    vy = euler(t, vy, lambda t, vy: -g, dt)
    t += dt

# === Plot Trajectory and Comparisons ===
plt.figure(figsize=(14, 4))

# y vs x
plt.subplot(1, 3, 1)
plt.plot(X, Y,)
plt.title("Trajectory (y vs x)")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt. grid()

# y vs t
plt.subplot(1, 3, 2)
plt.plot(T, Y)
plt.title("Height vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.grid()

# x vs t
plt.subplot(1, 3, 3)
plt.plot(T, X)
plt.title("Distance vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")

plt.tight_layout()
plt.show()

print("simulation values")
print(f"Range: {X[-1]:.2f} m")
print(f"Max Height: {max(Y):.2f} m")
print(f"Time of Flight: {T[-1]:.2f} s")

# === Free Fall Case ===
y = 100  # dropped from 100 meters
vy = 0
t = 0

Yf, Tf = [], []

while y >= 0:
    Yf.append(y)
    Tf.append(t)
    y = euler(t, y, lambda t, y: vy, dt)
    vy = euler(t, vy, lambda t, vy: -g, dt)
    t += dt

plt.plot(Tf, Yf)
plt.title("Free Fall (y vs t)")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.grid()
plt.show()

# === With Air Resistance ===
k = 0.1  # air resistance coefficient
m = 1.0  # mass

x, y = 0, 0
vx, vy = vx0, vy0
t = 0

Xa, Ya = [], []

while y >= 0:
    Xa.append(x)
    Ya.append(y)

    ax = lambda t, vx: -k * vx / m
    ay = lambda t, vy: -g - k * vy / m

    vx = euler(t, vx, ax, dt)
    vy = euler(t, vy, ay, dt)
    x = euler(t, x, lambda t, x: vx, dt)
    y = euler(t, y, lambda t, y: vy, dt)

    t += dt

# === Compare No Air vs With Air Resistance ===
plt.plot(X, Y, label='No Air Resistance')
plt.plot(Xa, Ya, label='With Air Resistance')
plt.title("Projectile with and without Air Resistance")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.legend()
plt.grid()
plt.show()