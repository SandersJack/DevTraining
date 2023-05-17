import uproot
import matplotlib.pyplot as plt

file = uproot.open("/home/jack/Code/DevTraining/Apps/Orbits/Oribts.root")

fx_earth = file["Data"]["Earth/Planets/fPosition.fx"].array()
fy_earth = file["Data"]["Earth/Planets/fPosition.fy"].array()

fx_mars = file["Data"]["Mars/Planets/fPosition.fx"].array()
fy_mars = file["Data"]["Mars/Planets/fPosition.fy"].array()

fig = plt.figure(figsize=(10,10))
plt.scatter(fx_earth,fy_earth)
plt.scatter(fx_mars,fy_mars)
plt.show()