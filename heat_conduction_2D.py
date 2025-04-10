#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Parameters
Lx = 1.0  # Length of the plate in the x-direction
Ly = 1.0  # Length of the plate in the y-direction
T_initial = 0.0  # Initial temperature
T_boundary = 100.0  # Boundary temperature
k = 1.0  # Thermal conductivity
alpha = 0.01  # Thermal diffusivity
t_max = 1.0  # Maximum time
dt = 0.001  # Time step
dx = 0.1  # Spatial step in the x-direction
dy = 0.1  # Spatial step in the y-direction

# Grid parameters
Nx = int(Lx / dx) + 1
Ny = int(Ly / dy) + 1
Nt = int(t_max / dt) + 1

# Initialize temperature array
T = np.ones((Nx, Ny)) * T_initial

# Boundary conditions
T[:, 0] = T_boundary  # Bottom boundary
T[:, -1] = T_boundary  # Top boundary
T[0, :] = T_boundary  # Left boundary
T[-1, :] = T_boundary  # Right boundary

# Construct original matrix
A = np.zeros((Nx * Ny, Nx * Ny))
for i in range(Nx):
    for j in range(Ny):
        idx = i * Ny + j
        A[idx, idx] = 1 + 4 * alpha * dt / (dx ** 2) + 4 * alpha * dt / (dy ** 2)
        if i > 0:
            A[idx, idx - Ny] = -alpha * dt / (dx ** 2)
        if i < Nx - 1:
            A[idx, idx + Ny] = -alpha * dt / (dx ** 2)
        if j > 0:
            A[idx, idx - 1] = -alpha * dt / (dy ** 2)
        if j < Ny - 1:
            A[idx, idx + 1] = -alpha * dt / (dy ** 2)

# Print original matrix
print("Original Matrix:")
print(A)

# Time-stepping loop
for n in range(1, Nt):
    # Solve for next time step using the original matrix A
    T = np.linalg.solve(A, T.flatten()).reshape((Nx, Ny))

# Print final temperature distribution
print("\nFinal Temperature Distribution on the Plate:")
print(T)

# Plotting
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, T, cmap='hot')
plt.colorbar(label='Temperature')
plt.title('Temperature Distribution on the Plate')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
    


# In[ ]:




