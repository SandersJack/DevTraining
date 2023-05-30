import uproot
import matplotlib.pyplot as plt

file = uproot.open("/home/jack/Code/DevTraining/Apps/Orbits/proton.root")

fx_earth = file["Data"]["Earth/Planets/fPosition.fx"].array()
fy_earth = file["Data"]["Earth/Planets/fPosition.fy"].array()

fx_mars = file["Data"]["Mars/Planets/fPosition.fx"].array()
fy_mars = file["Data"]["Mars/Planets/fPosition.fy"].array()

fx_Jupiter = file["Data"]["Jupiter/Planets/fPosition.fx"].array()
fy_Jupiter = file["Data"]["Jupiter/Planets/fPosition.fy"].array()

fx_Saturn = file["Data"]["Saturn/Planets/fPosition.fx"].array()
fy_Saturn = file["Data"]["Saturn/Planets/fPosition.fy"].array()

fx_Uranus = file["Data"]["Uranus/Planets/fPosition.fx"].array()
fy_Uranus = file["Data"]["Uranus/Planets/fPosition.fy"].array()

fx_Neptune = file["Data"]["Neptune/Planets/fPosition.fx"].array()
fy_Neptune = file["Data"]["Neptune/Planets/fPosition.fy"].array()

fx_moon = file["Data"]["Moon/fSunPosition.fx"].array()
fy_moon = file["Data"]["Moon/fSunPosition.fy"].array()

fx_sat = file["Data"]["Enterprise/fPosition/fPosition.fx"].array()
fy_sat = file["Data"]["Enterprise/fPosition/fPosition.fy"].array()

fig = plt.figure(figsize=(10,10))
plt.scatter(fx_moon,fy_moon)
plt.scatter(fx_earth,fy_earth)
plt.scatter(fx_mars,fy_mars)
plt.scatter(fx_Jupiter,fy_Jupiter)
plt.scatter(fx_Saturn,fy_Saturn)
plt.scatter(fx_Uranus,fy_Uranus)
plt.scatter(fx_Neptune,fy_Neptune)
plt.scatter(fx_sat,fy_sat)
#plt.scatter(fx_moon,fy_moon)
plt.scatter(0,0)
plt.show()