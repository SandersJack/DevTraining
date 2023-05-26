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

SiType = 0 # 0 = 3mm, 1 = 6mm, 2 = 9mm

SpotRadius = 0.30 * m

if(SiType == 0):
    SensorWidth = 0.003 * m 
    cen_fac = 18/3
    supercell_fac = 75
    nRow = 34
    channels_1 = 32346
elif SiType == 1:
    SensorWidth = 0.006 * m 
    cen_fac = 18/6
    supercell_fac = 37
    nRow = 17
    channels_1 = 8304
elif SiType == 2:
    SensorWidth = 0.009 * m
    cen_fac = 18/9
    supercell_fac = 25
    nRow = 12
    channels_1 = 3924

ConeInputRadius = 0.5 * SensorWidth

nPM = 0
#nRow = 12
nSuperCellinRow = [None]*nRow

PM_positions = [[0 for i in range(2)] for i in range(channels_1)]#8496)]

cell_dist = [None]*nRow

x_Center = 0
y_Center = 0

for i in range(nRow):
    nSuperCellinRow[i] = 0
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
        rectangle1 = plt.Rectangle((x-x_center*shiftx,y-y_center*shifty), SensorWidth/2, SensorWidth/2, fc=col)
        rectangle2 = plt.Rectangle((x-x_center*shiftx,y-y_center*shifty), SensorWidth/2, -SensorWidth/2, fc=col)
        rectangle3 = plt.Rectangle((x-x_center*shiftx,y-y_center*shifty), -SensorWidth/2, SensorWidth/2, fc=col)
        rectangle4 = plt.Rectangle((x-x_center*shiftx,y-y_center*shifty), -SensorWidth/2, -SensorWidth/2, fc=col)
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

for k in range(nRow):
      #first half
    nSuperCellinRow[k] = 0
    x_width = np.sqrt(SpotRadius**2 - ((k)*3*SensorWidth)**2) 

    while((nSuperCellinRow[k] + 1) * SensorWidth * 3/3 < 2*x_width+(SensorWidth)):
        nSuperCellinRow[k] +=1
    nSuperCellinRow[k] +=1
    
    if(k != 0):
        cell_dist[k] = int(np.floor((300-x_width) / (SensorWidth)))

    if(k == 0):
        x_center = 600 - (nSuperCellinRow[k]) * SensorWidth * 3/3 /2 -10
        #print(x_center)
    
    triCell = 0
    if k%2 == 0:
        for l in range(nSuperCellinRow[k]):
            for m in range(0,3):
                for n in range(-1,0):
                    
                    PM_positions[nPM][0] = (n + l + cell_dist[k])*SensorWidth;
                    PM_positions[nPM][1] = (m + k*3)*SensorWidth; #SensorWidth*m + SensorWidth*k*3
                    fPMsIDs[n + l*3 + 3*cell_dist[k]][m + k*3] = nPM;
                    #plot(PM_positions[nPM][0],PM_positions[nPM][1],n,m,l,k,nPM)
                    nPM += 1
                    if nPM ==1:
                        x_center = PM_positions[nPM-1][0] + 300
    else:
        for l in range(nSuperCellinRow[k],0,-1):
            for m in range(0,3):
                for n in range(-1,0):
                    
                    PM_positions[nPM][0] = (n + l + cell_dist[k]-1)*SensorWidth;
                    PM_positions[nPM][1] = (m + k*3)*SensorWidth; #SensorWidth*m + SensorWidth*k*3
                    fPMsIDs[n + l*3 + 3*cell_dist[k]][m + k*3] = nPM;
                    #plot(PM_positions[nPM][0],PM_positions[nPM][1],n,m,l,k,nPM)
                    nPM += 1
                    if nPM ==1:
                        x_center = PM_positions[nPM-1][0] + 300
            #print(triCell)      
#end first half
for j in range(nRow): 
    triCell = 0
    if j%2 == 0:
        for l in range(nSuperCellinRow[j]):
            for m in range(0,3):
                for n in range(-1,0):
                    PM_positions[nPM][0] = (n + l + cell_dist[j])*SensorWidth;
                                    
                    PM_positions[nPM][1] = -(m + j*3)*SensorWidth; #SensorWidth*m + SensorWidth*k*3
                    
                    fPMsIDs[n + l*3 + 3*cell_dist[j]+ 300][m + j*3 + 300] = nPM;
                    plot(PM_positions[nPM][0],PM_positions[nPM][1],n,m,l,k,nPM)
                    nPM += 1
                    #print(n + l*3 + 3*cell_dist[j] - triCell+ 300)
    else:
        for l in range(nSuperCellinRow[j],0,-1):
            for m in range(0,3):
                for n in range(-1,0):
                    PM_positions[nPM][0] = (n + l + cell_dist[j]-1)*SensorWidth;       
                    PM_positions[nPM][1] = -(m + j*3)*SensorWidth; #SensorWidth*m + SensorWidth*k*3
                    
                    fPMsIDs[n + l*3 + 3*cell_dist[j]+ 300][m + j*3 + 300] = nPM;
                    plot(PM_positions[nPM][0],PM_positions[nPM][1],n,m,l,k,nPM)
                    nPM += 1
print(nPM)
y_center = 0

fGeoIDs = [0]*channels_1

SCID = 0
UpDwID = 0
PMinSC = 0

for iPM in range(nPM):
    break
    #PMsPositions[iPM].Set(PM_positions[iPM][0] - x_Center, PM_positions[iPM][1] - y_Center);
    #    G4cout<<iPM<<"\t"<<PM_positions[iPM][0]-x_Center<<"\t"<<PM_positions[iPM][1]-y_Center<<G4endl;
    if(iPM < channels_1/2):
        UpDwID = 0
        SCID = int(iPM / 8)
    else:
        UpDwID = 1
        SCID = int((iPM - (channels_1/2)) / 8)

    

    PMinSC = iPM - (SCID * 8 + channels_1/2 * UpDwID)
    fGeoIDs[iPM] = UpDwID * 10000 + SCID * 100 + PMinSC; 

    #print(iPM,UpDwID,SCID,PMinSC)
    

#exit(0)
#print(fPMsIDs)
#x_center = 297
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
        rectangle1 = plt.Rectangle((PM_positions[i][0]-x_center,PM_positions[i][1]-y_center), SensorWidth/2, SensorWidth/2, fc=col,angle=ang)
        rectangle2 = plt.Rectangle((PM_positions[i][0]-x_center,PM_positions[i][1]-y_center), SensorWidth/2, -SensorWidth/2, fc=col,angle=ang)
        rectangle3 = plt.Rectangle((PM_positions[i][0]-x_center,PM_positions[i][1]-y_center), -SensorWidth/2, SensorWidth/2, fc=col,angle=ang)
        rectangle4 = plt.Rectangle((PM_positions[i][0]-x_center,PM_positions[i][1]-y_center), -SensorWidth/2, -SensorWidth/2, fc=col,angle=ang)
        #plt.plot(x,y)
        plt.gca().add_patch(rectangle1)
        plt.gca().add_patch(rectangle2)
        plt.gca().add_patch(rectangle3)
        plt.gca().add_patch(rectangle4)
        #plt.draw()

        if ((i)%3 == 2):
            #print(i)
            if col == 'red':
                col='green'
            else:
                col='red'

plt.gca().add_patch(circle)
plt.savefig('SiPM_new_{}.png'.format(SiType))
plt.show()