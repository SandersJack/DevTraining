import uproot
import matplotlib.pyplot as plt

file = uproot.open("/home/jack/Code/DevTraining/Apps/Orbits/proton.root")

keys = file["Data"].keys()

earth = True
try:
    fx_earth = file["Data"]["Earth/Planets/fPosition.fx"].array()
    fy_earth = file["Data"]["Earth/Planets/fPosition.fy"].array()
except uproot.exceptions.KeyInFileError:
    earth = False

mars = True
try:
    fx_mars = file["Data"]["Mars/Planets/fPosition.fx"].array()
    fy_mars = file["Data"]["Mars/Planets/fPosition.fy"].array()
except uproot.exceptions.KeyInFileError:
    mars = False

jupiter = True
try:
    fx_Jupiter = file["Data"]["Jupiter/Planets/fPosition.fx"].array()
    fy_Jupiter = file["Data"]["Jupiter/Planets/fPosition.fy"].array()
except uproot.exceptions.KeyInFileError:
    jupiter = False

Saturn = True
try:
    fx_Saturn = file["Data"]["Saturn/Planets/fPosition.fx"].array()
    fy_Saturn = file["Data"]["Saturn/Planets/fPosition.fy"].array()
except uproot.exceptions.KeyInFileError:
    Saturn = False

Uranus = True
try:
    fx_Uranus = file["Data"]["Uranus/Planets/fPosition.fx"].array()
    fy_Uranus = file["Data"]["Uranus/Planets/fPosition.fy"].array()
except uproot.exceptions.KeyInFileError:
    Uranus = False

Neptune = True
try:
    fx_Neptune = file["Data"]["Neptune/Planets/fPosition.fx"].array()
    fy_Neptune = file["Data"]["Neptune/Planets/fPosition.fy"].array()
except uproot.exceptions.KeyInFileError:
    Neptune = False

Mercury = True
try:
    fx_Mercury = file["Data"]["Mercury/Planets/fPosition.fx"].array()
    fy_Mercury = file["Data"]["Mercury/Planets/fPosition.fy"].array()
except uproot.exceptions.KeyInFileError:
    Mercury = False

venus = True
try:
    fx_venus = file["Data"]["Venus/Planets/fPosition.fx"].array()
    fy_venus = file["Data"]["Venus/Planets/fPosition.fy"].array()
except uproot.exceptions.KeyInFileError:
    venus = False

fx_moon = file["Data"]["Moon/fSunPosition.fx"].array()
fy_moon = file["Data"]["Moon/fSunPosition.fy"].array()

fx_sat = file["Data"]["Enterprise/fPosition/fPosition.fx"].array()
fy_sat = file["Data"]["Enterprise/fPosition/fPosition.fy"].array()

fig = plt.figure(figsize=(10,10))
plt.scatter(fx_moon,fy_moon)
if earth:
    plt.scatter(fx_earth,fy_earth)
if mars:
    plt.scatter(fx_mars,fy_mars)
if jupiter:
    plt.scatter(fx_Jupiter,fy_Jupiter)
if Saturn:
    plt.scatter(fx_Saturn,fy_Saturn)
if Uranus:
    plt.scatter(fx_Uranus,fy_Uranus)
if Neptune:
    plt.scatter(fx_Neptune,fy_Neptune)
if venus:
    plt.scatter(fx_venus,fy_venus)
if earth:
    plt.scatter(fx_Mercury,fy_Mercury)
plt.scatter(fx_sat,fy_sat)
#plt.scatter(fx_moon,fy_moon)
plt.scatter(0,0)
plt.show()