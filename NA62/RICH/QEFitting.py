import matplotlib.pyplot as plt
import numpy as np

fwavelength = [280,300, 340, 360, 400, 460, 500, 600, 650, 700, 800]

fpoints = [0.05, 0.22, 0.28, 0.28, 0.35, 0.40, 0.38, 0.26, 0.20, 0.15, 0.08]

z = np.polyfit(fwavelength[0:2],fpoints[0:2],1)
z1 = np.polyfit(fwavelength[1:3],fpoints[1:3],1)
z2 = np.polyfit(fwavelength[3:7],fpoints[3:7],2)
z3 = np.polyfit(fwavelength[8:],fpoints[8:],4)

z_ = np.polyfit(fwavelength,fpoints,8)

xz = np.linspace(fwavelength[0],fwavelength[1],6)
xz1 = np.linspace(fwavelength[1],fwavelength[2],6)
xz2 = np.linspace(fwavelength[3],fwavelength[6],50)
xz3 = np.linspace(fwavelength[6],fwavelength[-1],50)

xz_ = np.linspace(fwavelength[0],fwavelength[-1],100)

print(fwavelength[3:6])
fig = plt.figure(figsize=(5,5))

print(z)
print(z1)
print(z2)
print(z3)


plt.plot(fwavelength, fpoints)
plt.plot(xz,np.polyval(z, xz))
plt.plot(xz1,np.polyval(z1, xz1))
plt.plot(xz2,np.polyval(z2, xz2))
plt.plot(xz3,np.polyval(z3, xz3))
plt.grid()
plt.show()