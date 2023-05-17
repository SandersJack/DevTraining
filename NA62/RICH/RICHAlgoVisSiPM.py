import numpy as np
import matplotlib.pyplot as plt

m = 1000
mm = 2

fPMsIDs = [None]*1000
for iID in range(1000):
    fPMsIDs[iID] = [None]*1000
for iID1 in range(1000):
    for iID2 in range(1000):
        fPMsIDs[iID1][iID2] = -1

SiType = 1 # 0 = 3mm, 1 = 6mm, 2 = 9mm

SpotRadius = 0.30 * m

if(SiType == 0):
    ConeInputDiameter = 0.003 * m 
    cen_fac = 18/3
    supercell_fac = 75
    nRow = 37
    channels_1 = 33600
elif SiType == 1:
    ConeInputDiameter = 0.006 * m 
    cen_fac = 18/6
    supercell_fac = 37
    nRow = 17
    channels_1 = 10000#8496 
elif SiType == 2:
    ConeInputDiameter = 0.009 * m
    cen_fac = 18/9
    supercell_fac = 25
    nRow = 12
    channels_1 = 3824

ConeInputRadius = 0.5 * ConeInputDiameter
HoneyCombDistance = ConeInputRadius * np.sqrt(3) 

nPM = 0
#nRow = 12
nSuperCellinRow = [None]*nRow
nTriSuperCellinRow = [None]*nRow

PM_positions = [[0 for i in range(2)] for i in range(channels_1)]#8496)]
alpha = np.arctan(HoneyCombDistance / (5 * ConeInputRadius))
x_pos = ConeInputRadius
y_pos = 2 * (ConeInputRadius + HoneyCombDistance)

x_pos_trasf = x_pos * np.cos(alpha) + y_pos * np.sin(alpha)
y_pos_trasf = -x_pos * np.sin(alpha) + y_pos * np.cos(alpha)
Row_distance = np.sqrt(pow(x_pos_trasf, 2) + pow(y_pos_trasf, 2))

x_center_tmp = 30 * ConeInputRadius * cen_fac
y_center_tmp = -6 * HoneyCombDistance * cen_fac


angular_coeff = 3.141592654 / 2 - alpha
q = (-(3.141592654 / 2 - alpha) * x_center_tmp + y_center_tmp)
cell_dist = [None]*nRow

x_center_row0_up = 0
y_center_row0_up = 0
x_center_row0_down = 0
y_center_row0_down = 0

x_Center = 0
y_Center = 0

for i in range(nRow):
    nSuperCellinRow[i] = 0
    nTriSuperCellinRow[i] = 0
    cell_dist[i] = 0

plo = 0
animate = False
x_center = 285
y_center = 0


if animate:
    fig = plt.figure(figsize=(5,5))

    plt.xlim(-400,400)
    plt.ylim(-400,400)

    

    circle = plt.Circle((0,0),SpotRadius, fc="white",ec="blue")
    plt.gca().add_patch(circle)
    
def plot(x,y,n,m,l,k,i):
    if animate:
        #print(k,l,m,n)
        shiftx = 1
        shifty = 1
        if l%2 == 0:
            col = "red"
        else:
            col = "green"
        #circle = plt.Circle((x-x_center,y-y_center),7.5, fc=col,ec="blue")
        rectangle1 = plt.Rectangle((x-x_center*shiftx,y-y_center*shifty), 3, 3, fc=col)
        rectangle2 = plt.Rectangle((x-x_center*shiftx,y-y_center*shifty), 3, -3, fc=col)
        rectangle3 = plt.Rectangle((x-x_center*shiftx,y-y_center*shifty), -3, 3, fc=col)
        rectangle4 = plt.Rectangle((x-x_center*shiftx,y-y_center*shifty), -3, -3, fc=col)
        #plt.plot(x,y)
        plt.gca().add_patch(rectangle1)
        plt.gca().add_patch(rectangle2)
        plt.gca().add_patch(rectangle3)
        plt.gca().add_patch(rectangle4)
        plt.pause(0.0001)
        if plo == 0:
            pass
        else:
            pass
            #plt.draw()

for k in range(nRow):  #first half
    Chord = 2 * np.sqrt((SpotRadius - Row_distance * k) * (2 * SpotRadius - (SpotRadius - Row_distance * k)))
    nSuperCellinRow[k] = 0
    nTriSuperCellinRow[k] = 0
    x_width = np.sqrt(SpotRadius**2 - (k*3*ConeInputDiameter)**2) 

    while((nSuperCellinRow[k] + 1) * ConeInputDiameter * 8/3 < 2*x_width+10):
        nSuperCellinRow[k] +=1

    #
    
    #exit(0)
    #print(nSuperCellinRow)

    if(k != 0):
        x_width = np.sqrt(SpotRadius**2 - (k*3*ConeInputDiameter)**2) 
        cell_dist[k] = int(np.floor((300-x_width) / (3*ConeInputDiameter)))

    if(k == 0):
        x_center = 600 - (nSuperCellinRow[k]) * ConeInputDiameter * 8/3 /2
        print(x_center)
    
    triCell = 0

    for l in range(nSuperCellinRow[k]):
        for m in range(0,3):
            for n in range(-1,2):
                if (l%3 == 0):
                    if (m == 2 and n==1):
                        continue
                    PM_positions[nPM][0] = ConeInputDiameter*n + ConeInputDiameter*l*3 + 3*ConeInputDiameter*cell_dist[k] - triCell*ConeInputDiameter
                    PM_positions[nPM][1] = ConeInputDiameter*m + ConeInputDiameter*k*3
                    
                    plot(PM_positions[nPM][0],PM_positions[nPM][1],n,m,l,k,nPM)
                    plo +=1
                    fPMsIDs[n + 5 * l + 1 * k + 5 * cell_dist[k] + 100][m - 1 * l + 3 * k - 1 * cell_dist[k] + 100] = nPM
                    nPM += 1   
                    print(1, nPM ,nPM%8)
                if (l%3 == 1):
                    
                    if (m == 1 and n==1):
                        continue
                    PM_positions[nPM][0] = ConeInputDiameter*n + ConeInputDiameter*l*3 + 3*ConeInputDiameter*cell_dist[k] - triCell*ConeInputDiameter
                    PM_positions[nPM][1] = ConeInputDiameter*m + ConeInputDiameter*k*3
                    if (m ==2):
                        PM_positions[nPM][0] = ConeInputDiameter*n + ConeInputDiameter*l*3 + 3*ConeInputDiameter*cell_dist[k] - ConeInputDiameter - triCell*ConeInputDiameter
                    
                    plot(PM_positions[nPM][0],PM_positions[nPM][1],n,m,l,k,nPM)
                    plo +=1
                    fPMsIDs[n + 5 * l + 1 * k + 5 * cell_dist[k] + 100][m - 1 * l + 3 * k - 1 * cell_dist[k] + 100] = nPM
                    nPM += 1 
                    print(2, nPM, nPM%8)
                if (l%3 == 2):
                    if (m == 0 and n==-1):
                        continue
                    PM_positions[nPM][0] = ConeInputDiameter*n + ConeInputDiameter*l*3 + 3*ConeInputDiameter*cell_dist[k] - ConeInputDiameter - triCell*ConeInputDiameter
                    PM_positions[nPM][1] = ConeInputDiameter*m + ConeInputDiameter*k*3
                    
                    plot(PM_positions[nPM][0],PM_positions[nPM][1],n,m,l,k,nPM)
                    plo +=1
                    fPMsIDs[n + 5 * l + 1 * k + 5 * cell_dist[k] + 100][m - 1 * l + 3 * k - 1 * cell_dist[k] + 100] = nPM
                    nPM += 1 
                    print(3, nPM ,nPM%8)  
        if l%3 == 2:
            triCell += 1  


            #print(triCell)      

#end first half
for j in range(nRow): 
    
    triCell = 0
    for l in range(nSuperCellinRow[j]):

        for m in range(0,3):
            for n in range(-1,2):
                if (l%3 == 0):
                    if (m == 2 and n==1):
                        continue
                    PM_positions[nPM][0] = (ConeInputDiameter*n + ConeInputDiameter*l*3 + 3*ConeInputDiameter*cell_dist[j] - triCell*ConeInputDiameter)
                    PM_positions[nPM][1] = -(ConeInputDiameter*m + ConeInputDiameter*j*3)
                    
                    plot(PM_positions[nPM][0],PM_positions[nPM][1],n,m,l,k,nPM)
                    plo +=1
                    fPMsIDs[n + 5 * l + 1 * j + 5 * cell_dist[j] + 100][m - 1 * l + 3 * j - 1 * cell_dist[j] + 100] = nPM
                    nPM += 1   
                    print(1, nPM ,nPM%8)
                if (l%3 == 1):
                    
                    if (m == 1 and n==1):
                        continue
                    PM_positions[nPM][0] = (ConeInputDiameter*n + ConeInputDiameter*l*3 + 3*ConeInputDiameter*cell_dist[j] - triCell*ConeInputDiameter)
                    PM_positions[nPM][1] = -(ConeInputDiameter*m + ConeInputDiameter*j*3)
                    if (m ==2):
                        PM_positions[nPM][0] = (ConeInputDiameter*n + ConeInputDiameter*l*3 + 3*ConeInputDiameter*cell_dist[j] - ConeInputDiameter - triCell*ConeInputDiameter)
                    
                    plot(PM_positions[nPM][0],PM_positions[nPM][1],n,m,l,k,nPM)
                    plo +=1
                    fPMsIDs[n + 5 * l + 1 * j + 5 * cell_dist[j] + 100][m - 1 * l + 3 * k - 1 * cell_dist[j] + 100] = nPM
                    nPM += 1 
                    print(2, nPM, nPM%8)
                if (l%3 == 2):
                    if (m == 0 and n==-1):
                        continue
                    PM_positions[nPM][0] = (ConeInputDiameter*n + ConeInputDiameter*l*3 + 3*ConeInputDiameter*cell_dist[j] - ConeInputDiameter - triCell*ConeInputDiameter)
                    PM_positions[nPM][1] = -(ConeInputDiameter*m + ConeInputDiameter*j*3)
                    
                    plot(PM_positions[nPM][0],PM_positions[nPM][1],n,m,l,k,nPM)
                    plo +=1
                    fPMsIDs[n + 5 * l + 1 * j + 5 * cell_dist[j] + 100][m - 1 * l + 3 * k - 1 * cell_dist[j] + 100] = nPM
                    nPM += 1 
                    print(3, nPM ,nPM%8)  
        if l%3 == 2:
            triCell += 1  

'''
        #PM_positions[nPM][0] = (n + 5 * l - 1 * (j + 1) + 5 * (supercell_fac - nSuperCellinRow[j] - cell_dist[j])) * ConeInputRadius
        #PM_positions[nPM][1] = (m - 1 * l - 3 * (j + 1) - 1 * (supercell_fac - nSuperCellinRow[j] - cell_dist[j])) * HoneyCombDistance
PM_positions[nPM][0] = (ConeInputDiameter*n + ConeInputDiameter*l*3 + 3*ConeInputDiameter*cell_dist[j])
PM_positions[nPM][1] = -(ConeInputDiameter*m + ConeInputDiameter*j*3 + ConeInputDiameter) 
plot(PM_positions[nPM][0],PM_positions[nPM][1],n,m,l,k)
#print(PM_positions[nPM][0],PM_positions[nPM][1])
plo +=1
fPMsIDs[n + 5 * l - 1 * (j + 1) + 5 * (37 - nSuperCellinRow[j] - cell_dist[j]) + 100][m - 1 * l - 3 * (j + 1) - 1 * (37 - nSuperCellinRow[j] - cell_dist[j])+ 100] = nPM
nPM += 1

'''
x_center = 288
y_center = 0
ang = 0
print(nPM)
if not animate:
    print("No Animate")
    fig = plt.figure(figsize=(20,20))
    plt.xlim(-400,400)
    plt.ylim(-400,400)
    circle = plt.Circle((0,0),SpotRadius, fc="white",ec="blue",alpha=0.5)
    col = 'red'
    for i in range(len(PM_positions)):
        

        
        #print(PM_positions[i][0],PM_positions[i][1])
        #print(i)
        rectangle1 = plt.Rectangle((PM_positions[i][0]-x_center,PM_positions[i][1]-y_center), ConeInputDiameter/2, ConeInputDiameter/2, fc=col,angle=ang)
        rectangle2 = plt.Rectangle((PM_positions[i][0]-x_center,PM_positions[i][1]-y_center), ConeInputDiameter/2, -ConeInputDiameter/2, fc=col,angle=ang)
        rectangle3 = plt.Rectangle((PM_positions[i][0]-x_center,PM_positions[i][1]-y_center), -ConeInputDiameter/2, ConeInputDiameter/2, fc=col,angle=ang)
        rectangle4 = plt.Rectangle((PM_positions[i][0]-x_center,PM_positions[i][1]-y_center), -ConeInputDiameter/2, -ConeInputDiameter/2, fc=col,angle=ang)
        #plt.plot(x,y)
        plt.gca().add_patch(rectangle1)
        plt.gca().add_patch(rectangle2)
        plt.gca().add_patch(rectangle3)
        plt.gca().add_patch(rectangle4)
        #plt.draw()

        if ((i)%8 == 7):
            #print(i)
            if col == 'red':
                col='green'
            else:
                col='red'

plt.gca().add_patch(circle)
plt.savefig('SiPM_new2.png')
plt.show()