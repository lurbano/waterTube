import numpy as np 
import time 
from ezGraph import *

def myAvg(lst):
    # sum 
    s = 0
    n = 0
    for i in lst:
        s = s + i
        n += 1
    return s/n

# Finite Difference Model

# PARAMETERS
dt = 1
nsteps = 30

r = 2.25    # radius (cm)
Qin = 30       # Volume inflow rate (dV/dt): (cubic cm / s)
h = 0       # Initial height (cm)
k = 0.0     # outflow rate constant

# EXPERIMENTAL DATA
x_measured = [1, 7, 12, 17, 22, 26]
y_measured = [0, 10, 20, 30, 40, 50]

# GRAPH
graph = ezGraphMM(xmin=0, xmax=100, 
                xLabel="Time (s)", 
                yLabel="Height (cm)",
                x_measured = x_measured,
                y_measured = y_measured)

graph.addModeled(0, h)             # add initial values


# TIME LOOP
for t in range(1, nsteps):
    modelTime = t * dt

    # Filling
    dh = Qin * dt / (np.pi * r**2)  # find the change in height
    h = h + dh                      # update height

    # Draining
    dVdt = -k * h
    dh = dVdt * dt / (np.pi * r**2)
    h = h + dh

    graph.addModeled(modelTime, h)
    graph.wait(0.01)

# DRAW GRAPH
graph.keepOpen()
    
