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


x = np.array([28.62,28.60,28.62,28.65,28.61,28.58])
y = np.array([81.62,81.64,81.58,81.61,81.61,81.65])
z = np.array([53.00,52.96,52.96,52.96,53.00,53.01])
w = np.array([14.67,14.70,14.70,14.70,14.67,14.69])
a1 = np.array([10.0,10.0,10.0,10.0,10.0,10.0])
a2 = np.array([100.0,100.0,100.0,100.0,100.0,100.0])

print(np.sum(x)/len(x))
print(np.sum(y)/len(y))
print(np.sum(z)/len(z))
print(np.sum(w)/len(w))


unsurex = unsure(x,0.683,1e-1,np.sqrt(3))
unsurey = unsure(y,0.683,1e-1,np.sqrt(3))
unsurez = unsure(z,0.683,1e-1,np.sqrt(3))
unsurew = unsure(w,0.683,1e-1,np.sqrt(3))
unsurea1 = unsure(a1,0.683,1e-1,np.sqrt(3))
unsurea2 = unsure(a2,0.683,1e-1,np.sqrt(3))
print(unsurex.unsure())
print(unsurey.unsure())
print(unsurea1.unsure())
print(unsurea2.unsure())

c = (0.25+52.982**2/90**2*0.25)/14.688
d = 52.982/180/14.688
print(c,d)
print(14.688*np.sqrt(2*c**2+2*d**2)*unsurea1.unsure())