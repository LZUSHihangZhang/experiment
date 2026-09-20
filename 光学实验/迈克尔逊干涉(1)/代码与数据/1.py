import numpy as np


class unsure:
    def __init__(self,x,p,delta,C):
        self.x = x
        self.p = p
        self.mean = np.sum(self.x)/len(self.x)
        self.delta = delta
        self.C = C

    def unsureA(self):
        Delta = self.x - self.mean
        Delta2 = Delta ** 2
        return np.sqrt(np.sum(Delta2) / (len(self.x) * (len(self.x) - 1))) * self.p

    def unsureB(self):
        return self.delta/self.C

    def unsure(self):
        return np.sqrt(self.unsureA()**2+self.unsureB()**2)


n = np.array([0,30,60,90])
x = np.array([46.21255,46.20297,46.19391,46.18468])
y = []
for i in range(3):
    y.append(x[i+1]-x[i])

print((x[3]+x[2]-x[1]-x[0]) /60)
print((-(x[3]+x[2]-x[1]-x[0]) / 60*1e6-632.8)/632.8)
print((-(x[3]-x[0])/45*1e6-632.8)/632.8)
p = np.sqrt(np.sum((y-np.mean(y))**2)/6)*1e6
q = 100/np.sqrt(3)
print(np.sqrt(np.sqrt(p**2+q**2)/15))