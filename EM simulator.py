import numpy as np
import matplotlib.pyplot as plt

# Constants
q = 1.6e-19  # Charge of the particle in coulombs
m = 1e-18  # Mass of the particle in kg
A = 0.5

# Initial conditions
v = np.array([0.05, 0.0005, 10000.0])  # Initial velocity in m/s
r = np.array([0.0, 0.0, 0.0])  # Initial position in m
B = np.array([A * r[1], A * r[0], 0])  # Magnetic field strength in tesla


t = np.linspace(0, 0.5, 1000)  # Time in seconds
dt = t[1] - t[0]


# Update the velocity (v = v0 + F/m*dt)
for i in range(1, len(t)):
    B = np.array([A * r[1], A * r[0], 0])
    F = q * np.cross(v, B)
    # print(F)
    for i in range(3):
        v[i] += F[i] / m * dt
        r[i] += v[i] * dt
    print(r)
