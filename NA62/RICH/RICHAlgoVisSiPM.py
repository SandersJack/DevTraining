import numpy as np
import matplotlib.pyplot as plt

m = 1000
mm = 1

fPMsIDs = [None]*1000
for iID in range(1000):
    fPMsIDs[iID] = [None]*1000
for iID1 in range(1000):
    for iID2 in range(1000):
        fPMsIDs[iID1][iID2] = -1


SpotRadius = 0.30 * m
ConeInputDiameter = 0.006 * m
ConeInputRadius = 0.5 * ConeInputDiameter
HoneyCombDistance = ConeInputRadius * np.sqrt(3) 

nPM = 0
nRow = 6
nSuperCellinRow = [None]*6

PM_positions = [[None]*2]*10000
alpha = np.arctan(HoneyCombDistance / (5 * ConeInputRadius))
x_pos = ConeInputRadius
y_pos = 2 * (ConeInputRadius + HoneyCombDistance)

x_pos_trasf = x_pos * np.cos(alpha) + y_pos * np.sin(alpha)
y_pos_trasf = -x_pos * np.sin(alpha) + y_pos * np.cos(alpha)
Row_distance = np.sqrt(pow(x_pos_trasf, 2) + pow(y_pos_trasf, 2))

x_center_tmp = 30 * ConeInputRadius
y_center_tmp = -6 * HoneyCombDistance

angular_coeff = 3.141592654 / 2 - alpha
q = -(3.141592654 / 2 - alpha) * x_center_tmp + y_center_tmp

cell_dist = [None]*6

x_center_row0_up = 0
y_center_row0_up = 0
x_center_row0_down = 0
y_center_row0_down = 0

x_Center = 0
y_Center = 0

for i in range(nRow):
    nSuperCellinRow[i] = 0
    cell_dist[i] = 0

plo = 0
animate = True
x_center = 243
y_center = -109.119


if animate:
    fig = plt.figure(figsize=(20,20))

    plt.xlim(-400,400)
    plt.ylim(-400,400)

    

    circle = plt.Circle((0,0),SpotRadius, fc="white",ec="blue")
    plt.gca().add_patch(circle)
    



def plot(x,y,n,m,l,k, col="red"):
    if animate:
        print(k,l,m,n)
        #circle = plt.Circle((x-x_center,y-y_center),7.5, fc=col,ec="blue")
        rectangle1 = plt.Rectangle((x-x_center,y-y_center), 3, 3, fc=col)
        rectangle2 = plt.Rectangle((x-x_center,y-y_center), 3, -3, fc=col)
        rectangle3 = plt.Rectangle((x-x_center,y-y_center), -3, 3, fc=col)
        rectangle4 = plt.Rectangle((x-x_center,y-y_center), -3, -3, fc=col)
        #plt.plot(x,y)
        plt.gca().add_patch(rectangle1)
        plt.gca().add_patch(rectangle2)
        plt.gca().add_patch(rectangle3)
        plt.gca().add_patch(rectangle4)
        plt.pause(0.0001)
        if plo == 0:
            pass
        else:
            plt.draw()
    

for k in range(nRow):  #first half

    Chord = 2 * np.sqrt((SpotRadius - Row_distance * k) * (2 * SpotRadius - (SpotRadius - Row_distance * k)))
    nSuperCellinRow[k] = 0

    if(k < 5):
        while((nSuperCellinRow[k] + 1) * 2 * (ConeInputRadius + HoneyCombDistance) < Chord + 22.):
            nSuperCellinRow[k] +=1
    else:
        while((nSuperCellinRow[k] + 1) * 2 * (ConeInputRadius + HoneyCombDistance) < Chord):
            nSuperCellinRow[k] +=1

    if(k != 0):
        x_center_r = (1 * k + 5 * nSuperCellinRow[k]) / 2 * ConeInputRadius
        y_center_r = (3 * k - nSuperCellinRow[k]) / 2 * HoneyCombDistance
        center_distance = abs(y_center_r - angular_coeff * x_center_r - q) / np.sqrt(1 + pow(angular_coeff, 2))
        
        cell_dist[k] = int(np.floor(center_distance / (2 * (ConeInputRadius + HoneyCombDistance)) + 0.2))
        
        

    for l in range(nSuperCellinRow[k]):

        if(k == 0 ):
            x_center_row0_up = x_center_row0_up + 5 * l * ConeInputRadius
            y_center_row0_up = y_center_row0_up - 1 * l * HoneyCombDistance

        for m in range(-1,2):
            for n in range(-(abs(m) + 1),(abs(m) + 1)+1):
                #print(n,(abs(m) + 1))
                if(m != 0):
                    if(0 == abs(n) % 2):
                        PM_positions[nPM][0] = (n + 5 * l + 1 * k + 5 * cell_dist[k]) * ConeInputRadius
                        PM_positions[nPM][1] = (m - 1 * l + 3 * k - 1 * cell_dist[k]) * HoneyCombDistance
                        print(k,l,m,n, nPM,PM_positions[nPM][0],PM_positions[nPM][1])
                        plot(PM_positions[nPM][0],PM_positions[nPM][1],n,m,l,k)
                        plo +=1
                        fPMsIDs[n + 5 * l + 1 * k + 5 * cell_dist[k] + 100][m - 1 * l + 3 * k - 1 * cell_dist[k] + 100] = nPM
                        nPM += 1
                    
                
                else:
                    if(0 != abs(n) % 2):
                        PM_positions[nPM][0] = (n + 5 * l + 1 * k + 5 * cell_dist[k]) * ConeInputRadius
                        PM_positions[nPM][1] = (m - 1 * l + 3 * k - 1 * cell_dist[k]) * HoneyCombDistance
                        plot(PM_positions[nPM][0],PM_positions[nPM][1],n,m,l,k, "green")
                        plo +=1
                        fPMsIDs[n + 5 * l + 1 * k + 5 * cell_dist[k] + 100][m - 1 * l + 3 * k - 1 * cell_dist[k] + 100] = nPM
                        nPM +=1
                    
        
    if k == 0: 
        x_center_row0_up = x_center_row0_up / nSuperCellinRow[k]
        y_center_row0_up = y_center_row0_up / nSuperCellinRow[k]

#end first half
'''
for j in range(nRow): 
    for l in range(nSuperCellinRow[j]):

        if j == 0:
            x_center_row0_down = x_center_row0_down + (5 * l - 1 * (j + 1)) * ConeInputRadius
            y_center_row0_down = y_center_row0_down - (1 * l + 3 * (j + 1)) * HoneyCombDistance

        for m in range(-1,2):
            for n in range(-(abs(m) + 1),(abs(m) + 1)+1):
                if(m):
                    if(0 == abs(n) % 2):
                        PM_positions[nPM][0] = (n + 5 * l - 1 * (j + 1) + 5 * (37 - nSuperCellinRow[j] - cell_dist[j])) * ConeInputRadius
                        PM_positions[nPM][1] = (m - 1 * l - 3 * (j + 1) - 1 * (37 - nSuperCellinRow[j] - cell_dist[j])) * HoneyCombDistance
                        plot(PM_positions[nPM][0],PM_positions[nPM][1],n,m,l,k)
                        plo +=1
                        fPMsIDs[n + 5 * l - 1 * (j + 1) + 5 * (37 - nSuperCellinRow[j] - cell_dist[j]) + 100][m - 1 * l - 3 * (j + 1) - 1 * (37 - nSuperCellinRow[j] - cell_dist[j])+ 100] = nPM
                        nPM += 1
            
                else:
                    if(0 != np.abs(n) % 2):
                        PM_positions[nPM][0] = (n + 5 * l - 1 * (j + 1) + 5 * (37 - nSuperCellinRow[j] - cell_dist[j])) * ConeInputRadius
                        PM_positions[nPM][1] = (m - 1 * l - 3 * (j + 1) - 1 * (37 - nSuperCellinRow[j] - cell_dist[j])) * HoneyCombDistance
                        plot(PM_positions[nPM][0],PM_positions[nPM][1],n,m,l,k,"green")
                        plo +=1
                        fPMsIDs[n + 5 * l - 1 * (j + 1) + 5 * (37 - nSuperCellinRow[j] - cell_dist[j]) + 100][m - 1 * l - 3 * (j + 1) - 1 * (37 - nSuperCellinRow[j] - cell_dist[j])+ 100] = nPM
                        nPM +=1
'''

if not animate:
    print("No Animate")
    fig = plt.figure(figsize=(20,20))
    for i in range(len(PM_positions)):
        print(PM_positions[i][0])
        print(i)
        rectangle1 = plt.Rectangle((PM_positions[i][0]-x_center,PM_positions[i][1]-y_center), 3, 3, fc="blue")
        rectangle2 = plt.Rectangle((PM_positions[i][0]-x_center,PM_positions[i][1]-y_center), 3, -3, fc="blue")
        rectangle3 = plt.Rectangle((PM_positions[i][0]-x_center,PM_positions[i][1]-y_center), -3, 3, fc="blue")
        rectangle4 = plt.Rectangle((PM_positions[i][0]-x_center,PM_positions[i][1]-y_center), -3, -3, fc="blue")
        #plt.plot(x,y)
        plt.gca().add_patch(rectangle1)
        plt.gca().add_patch(rectangle2)
        plt.gca().add_patch(rectangle3)
        plt.gca().add_patch(rectangle4)
        plt.draw()

plt.savefig('SiPM_1.png')
plt.show()