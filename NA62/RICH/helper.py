import numpy as np 
import math 
import matplotlib.pyplot as plt

def Gaus(x,mu,sig):

    f = (1/(sig*np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mu)/(sig))**2)

    return f

def eq(x):
    e = Gaus(x,0,0.12) + 0.1101571*Gaus(x, -0.1750211, 0.23) + 0.0290554*np.exp(1.03047*(0.557182-2*x))*(1-math.erfc((0.282630-x)/0.0885416)) + 0.0066920*Gaus(x, 1.47462, 0.13)

    return e

v = np.linspace(-1,2, 100)
y = []
for i in range(len(v)):
    y.append(eq(v[i]))

plt.plot(v,y)
plt.show()