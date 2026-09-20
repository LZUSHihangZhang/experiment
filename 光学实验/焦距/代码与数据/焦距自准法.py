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
        Delta2 = Delta**2
        return np.sqrt(np.sum(Delta2)/(len(self.x)*(len(self.x)-1)))*self.p


    def unsureB(self):
        return self.delta/self.C

    def unsure(self):
        return np.sqrt(self.unsureA()**2+self.unsureB()**2)



x = np.array([24.70,24.80,24.90,25.00,25.10,25.20,25.20,25.13,25.03,24.95,24.85,24.83])
unsurex = unsure(x,0.683,1e-1,np.sqrt(3))
y = np.ones(12)*10.00
unsurey = unsure(y,0.683,1e-1,np.sqrt(3))
print(unsurex.unsure())
print(unsurey.unsure())
print(np.sqrt(unsurex.unsure()**2+unsurey.unsure()**2))
print(np.sum(x-10)/len(x))