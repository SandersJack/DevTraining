import numpy as np
import matplotlib.pyplot as plt

m = 1000
mm = 2

fPMsIDs = [None]*500
for iID in range(500):
    fPMsIDs[iID] = [None]*500
for iID1 in range(500):
    for iID2 in range(500):
        fPMsIDs[iID1][iID2] = -1

SiType = 1 # 0 = 3mm, 1 = 6mm, 2 = 9mm

SpotRadius = 0.30 * m

if(SiType == 0):
    SensorWidth = 0.003 * m 
    cen_fac = 18/3
    supercell_fac = 75
    nRow = 34
    channels_1 = 32096
elif SiType == 1:
    SensorWidth = 0.006 * m 
    cen_fac = 18/6
    supercell_fac = 37
    nRow = 17
    channels_1 = 10000
elif SiType == 2:
    SensorWidth = 0.009 * m
    cen_fac = 18/9
    supercell_fac = 25
    nRow = 12
    channels_1 = 3824

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
    nSuperCellinRow[k] = 0
    x_width = np.sqrt(SpotRadius**2 - (k*3*SensorWidth)**2) 
    

    while((nSuperCellinRow[k] + 1) * SensorWidth * 8/3 < 2*x_width+(SensorWidth*1.6)):
        nSuperCellinRow[k] +=1


    #
    #print(nSuperCellinRow[k] * SensorWidth * 8/3)
    #exit(0)
    #print(nSuperCellinRow)

    if(k != 0):
        cell_dist[k] = int(np.floor((300-x_width) / (3*SensorWidth)))

    if(k == 0):
        x_center = 600 - (nSuperCellinRow[k]) * SensorWidth * 8/3 /2
        #print(x_center)
    
    triCell = 0

    for l in range(nSuperCellinRow[k]):
        for m in range(0,3):
            for n in range(-1,2):
                if (((l%3 == 0 and m == 2 and n==1) or (l%3 == 1 and m == 1 and n==1) or (l%3 == 2 and m == 0 and n==-1))):
                    continue
                if((l%3 == 1 and m==2) or (l%3==2)):
                    PM_positions[nPM][0] = (n + l*3 + 3*cell_dist[k] - triCell - 1)*SensorWidth;
                else:
                    PM_positions[nPM][0] = (n + l*3 + 3*cell_dist[k] - triCell)*SensorWidth;
                                
                PM_positions[nPM][1] = (m + k*3)*SensorWidth; #SensorWidth*m + SensorWidth*k*3
                
                if((l%3 == 1 and m==2) or (l%3==2)):
                    fPMsIDs[n + l*3 + 3*cell_dist[k] - triCell - 1 + 100][m + k*3 + 100] = nPM;
                else:
                    fPMsIDs[n + l*3 + 3*cell_dist[k] - triCell][m + k*3] = nPM;
                nPM += 1

                #print(PM_positions[nPM-1][0])
                #exit(0)
                #print(n + l*3 + 3*cell_dist[k] - triCell + 100,m + k*3 + 100)
                if nPM ==1:
                    x_center = PM_positions[nPM-1][0] + 300 - SensorWidth
        if l%3 == 2:
            triCell += 1 
            #print(triCell)      
#end first half
for j in range(nRow): 
    
    triCell = 0
    for l in range(nSuperCellinRow[j]):

        for m in range(0,3):
            for n in range(-1,2):
                if ((l%3 == 0 and m == 2 and n==1) or (l%3 == 1 and m == 1 and n==1) or (l%3 == 2 and m == 0 and n==-1)):
                    continue
                if((l%3 == 1 and m==2) or (l%3==2)):
                    PM_positions[nPM][0] = (n + l*3 + 3*cell_dist[j] - triCell - 1)*SensorWidth;
                else:
                    PM_positions[nPM][0] = (n + l*3 + 3*cell_dist[j] - triCell)*SensorWidth;
                                
                PM_positions[nPM][1] = -(m + j*3)*SensorWidth; #SensorWidth*m + SensorWidth*k*3
                
                if((l%3 == 1 and m==2) or (l%3==2)):
                    fPMsIDs[n + l*3 + 3*cell_dist[j] - triCell - 1 + 300][m + j*3 + 300] = nPM;
                else:
                    fPMsIDs[n + l*3 + 3*cell_dist[j] - triCell+ 300][m + j*3 + 300] = nPM;
                nPM += 1
                #print(n + l*3 + 3*cell_dist[j] - triCell+ 300)
        if l%3 == 2:
            triCell += 1  
print(nPM)
y_center = 0

fGeoIDs = [0]*channels_1

SCID = 0
UpDwID = 0
PMinSC = 0

for iPM in range(nPM):
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

        if ((i)%8 == 7):
            #print(i)
            if col == 'red':
                col='green'
            else:
                col='red'

plt.gca().add_patch(circle)
plt.savefig('SiPM_new_{}.png'.format(SiType))
plt.show()