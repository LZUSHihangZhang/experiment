import numpy as np


x1 = 20.125

x2 = 17.758

n = 1.516

d=abs(x2-x1)/(20*(n-1))
print(d)
u = 0.01/np.sqrt(3)
partial = 1/(20*(n-1))
print(d*np.sqrt(2*u**2*partial**2))