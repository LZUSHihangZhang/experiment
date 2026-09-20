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
