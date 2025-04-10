#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

#parameters
L = 1.0  #length of the rod
T_initial = 0.0  #initial temperature
T_boundary = 100.0  #boundary temperature
k = 1.0  #thermal conductivity
alpha = 0.01  #thermal diffusivity
t_max = 1.0  #maximum time
dt = 0.001  #time step
dx = 0.1  #spatial step

#grid parameters
Nx = int(L / dx) + 1
Nt = int(t_max / dt) + 1

#initialize temperature array
T = np.ones(Nx) * T_initial

#boundary conditions
T[0] = T_boundary  #left boundary
T[-1] = T_boundary  #right boundary

#construct original matrix
A = np.zeros((Nx, Nx))
for i in range(Nx):
    for j in range(Nx):
        if i == j:
            A[i, j] = 1 + 2 * alpha * dt / (dx ** 2)
        elif abs(i - j) == 1:
            A[i, j] = -alpha * dt / (dx ** 2)

#print original matrix
print("Original Matrix:")
print(A)

#time-stepping loop
for n in range(1, Nt):
    #solve for next time step using the original matrix A 
    T = np.linalg.solve(A, T)

#print final temperature distribution
print("\nFinal Temperature Distribution along the Rod:")
print(T)

# Plotting
x = np.linspace(0, L, Nx)

plt.figure(figsize=(8, 6))
plt.plot(x, T, 'b-', label='Temperature Distribution')
plt.title('Temperature Distribution along the Rod')
plt.xlabel('Position')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




