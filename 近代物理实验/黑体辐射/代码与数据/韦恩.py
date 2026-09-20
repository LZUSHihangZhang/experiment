import matplotlib.pyplot as plt
import numpy as np

L = np.array([1000,1006,1014,1020,1222],dtype=float)
T = np.array([2940,2860,2770,2720,2400],dtype=float)
A = L*T/1000000
print(A)
print(np.sqrt(np.sum((A-np.mean(A))**2)/(5*4)))