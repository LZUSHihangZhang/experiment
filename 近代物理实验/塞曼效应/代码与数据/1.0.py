import numpy as np

B = np.array([1.052,1.054,1.059])

a1 = np.array([1.12,1.12,1.12])
b1 = np.array([1.18,1.18,1.18])
c1 = np.array([1.23,1.23,1.23])

a2 = np.array([1.40,1.40,1.40])
b2 = np.array([1.45,1.45,1.46])
c2 = np.array([1.50,1.51,1.51])

R1 = b1.mean()
R2 = b2.mean()
print((R2**2 - R1**2)*4)
A = np.array([b1**2-a1**2,c1**2-b1**2,b2**2-a2**2,c2**2-b2**2]).reshape(-1)
B = 4*np.array([((a2+b2)/2)**2-((a1+b1)/2)**2,((c2+b2)/2)**2-((c1+b1)/2)**2]*2).reshape(-1)
print(A)
print(B)
Delta_D = A/(R2**2 - R1**2)/4/2*1e3
print(Delta_D)
print(Delta_D.mean())
print(Delta_D.mean()*4*np.pi*3*1e8/(B.mean()/2))