import numpy as np 
import math 
import matplotlib.pyplot as plt
'''
def Gaus(x,mu,sig):

    f = (1/(sig*np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mu)/(sig))**2)

    return f

def eq(x):
    e = Gaus(x,0,0.12) + 0.1101571*Gaus(x, -0.1750211, 0.23) + 0.0290554*np.exp(1.03047*(0.557182-2*x))*(1-math.erfc((0.282630-x)/0.0885416)) + 0.0066920*Gaus(x, 1.47462, 0.13)

    return e

def eq2(x):

    e = 10390*Gaus(x, -0.002503, 0.03187) + 2029*Gaus(x, 0.108, 0.120)

    return e

def eq3(x):

    e = Gaus(x,0, 0.1)

    return e

v = np.linspace(-1,2, 100)
y = []
for i in range(len(v)):
    y.append(eq3(v[i]))
'''
'''
r = 2150
r2 = 1200

posx = r * np.cos(np.pi+ -np.pi/12)
posy =  r * np.sin(np.pi+ -np.pi/12)

posx_in = r2 * np.cos(np.pi+ -np.pi/12)
posy_in =  r2 * np.sin(np.pi+ -np.pi/12)

points_x = [posx_in,posx]
points_y = [posy_in,posy]

a, b = np.polyfit(points_x, points_y, 1)

print(a,b)

yvals = a*np.array(points_x)+0
xvals = np.array(points_y)/a
#add line of best fit to plot
plt.plot(xvals, yvals)

plt.scatter(points_x,points_y)
plt.show()
'''
string = ''

for i in range(45*4):
    string += ' 2'

print(string)