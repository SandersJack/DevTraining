import uproot
import matplotlib.pyplot as plt

file = uproot.open("/home/jack/Code/DevTraining/Apps/Orbits/Oribts.root")

fx = file["Data"]["position/fx"].array()
fy = file["Data"]["position/fy"].array()

fig = plt.figure(figsize=(10,10))
plt.scatter(fx,fy)
plt.show()