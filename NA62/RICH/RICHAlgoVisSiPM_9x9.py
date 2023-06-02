import numpy as np
import matplotlib.pyplot as plt
import os

m = 1000
mm = 2


def DecodeChannelID(ChannelID):
    DiskID = np.floor(ChannelID / 100000)
    UpDownDiskID = np.floor((ChannelID % 100000) / 10000)
    SuperCellID = np.floor((ChannelID % 10000) / 10)
    OrSuperCellID = np.floor((ChannelID % 100) / 10)
    PmtID = np.floor(ChannelID % 10)
    
    return DiskID,UpDownDiskID,SuperCellID,OrSuperCellID,PmtID

SiType = 1 # 0 = 3mm, 1 = 6mm, 2 = 9mm

SpotRadius = 0.30 * m

if(SiType == 0):
    SensorWidth = 0.003 * m 
    cen_fac = 18/3
    supercell_fac = 75
    nRow = 34
    channels_1 = 32346
    id_length = 401
elif SiType == 1:
    SensorWidth = 0.006 * m 
    cen_fac = 18/6
    supercell_fac = 37
    nRow = 17
    channels_1 = 8304
    id_length = 301
elif SiType == 2:
    SensorWidth = 0.009 * m
    cen_fac = 18/9
    supercell_fac = 25
    nRow = 12
    channels_1 = 3924
    id_length = 271

fPMsIDs = [None]*id_length
for iID in range(id_length):
    fPMsIDs[iID] = [None]*id_length
for iID1 in range(id_length):
    for iID2 in range(id_length):
        fPMsIDs[iID1][iID2] = -1

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
                PM_positions[nPM][0] = (-1 + l + cell_dist[k])*SensorWidth;
                PM_positions[nPM][1] = (m + k*3)*SensorWidth; #SensorWidth*m + SensorWidth*k*3
                fPMsIDs[-1 + l + cell_dist[k]][m + k*3] = nPM;
                print(l)
                #print(-1 + l + cell_dist[k],m + k*3)
                plot(PM_positions[nPM][0],PM_positions[nPM][1],-1,m,l,k,nPM)
                nPM += 1
                if nPM ==1:
                    x_center = PM_positions[nPM-1][0] + 300
        exit(l)
                
    else:
        for l in range(nSuperCellinRow[k],0,-1):
            for m in range(0,3):
                PM_positions[nPM][0] = (l + cell_dist[k]-2)*SensorWidth;
                PM_positions[nPM][1] = (m + k*3)*SensorWidth; #SensorWidth*m + SensorWidth*k*3
                fPMsIDs[l + cell_dist[k]-2][m + k*3] = nPM;
                #print(-2 + l + cell_dist[k],m + k*3)
                #print(nPM)
                plot(PM_positions[nPM][0],PM_positions[nPM][1],-1,m,l,k,nPM)
                nPM += 1
                if nPM ==1:
                    x_center = PM_positions[nPM-1][0] + 300
            #print(triCell) 
            # 

#end first half
for j in range(nRow): 
    triCell = 0
    if j%2 == 0:
        for l in range(nSuperCellinRow[j]):
            for m in range(0,3):
                PM_positions[nPM][0] = (-1 + l + cell_dist[j])*SensorWidth;
                                
                PM_positions[nPM][1] = -(m + j*3)*SensorWidth; #SensorWidth*m + SensorWidth*k*3
                
                fPMsIDs[-1 + l + cell_dist[j]+ 200][m + j*3 + 200] = nPM;
                print(l + cell_dist[j] - 1 + 200,m + j*3 + 200)
                plot(PM_positions[nPM][0],PM_positions[nPM][1],-1,m,l,k,nPM)
                nPM += 1
                #print(n + l*3 + 3*cell_dist[j] - triCell+ 300)
    else:
        for l in range(nSuperCellinRow[j],0,-1):
            for m in range(0,3):
               
                PM_positions[nPM][0] = (l + cell_dist[j]-2)*SensorWidth;       
                PM_positions[nPM][1] = -(m + j*3)*SensorWidth; #SensorWidth*m + SensorWidth*k*3
                
                fPMsIDs[l + cell_dist[j] - 2 + 200][m + j*3 + 200] = nPM;
                print(l + cell_dist[j] - 2 + 200,m + j*3 + 200)
                plot(PM_positions[nPM][0],PM_positions[nPM][1],-1,m,l,k,nPM)
                nPM += 1

    #exit(0)
print(nPM)
y_center = 0

fGeoIDs = [0]*channels_1

SCID = 0
UpDwID = 0
PMinSC = 0

channel = []
channel_map = []
count = 0

count_sc = 0

pos = []
pos_map = []

pos_SC = []
pos_map_SC = []

supercell_map = []
supercell = []


with open('Channels_{}.txt'.format(SiType), 'w') as out:
    for iPM in range(nPM):
        
        
        #PMsPositions[iPM].Set(PM_positions[iPM][0] - x_Center, PM_positions[iPM][1] - y_Center);
        #    G4cout<<iPM<<"\t"<<PM_positions[iPM][0]-x_Center<<"\t"<<PM_positions[iPM][1]-y_Center<<G4endl;
        if(iPM < channels_1/2):
            UpDwID = 0
            SCID = int(iPM / 8)
        else:
            UpDwID = 1
            SCID = int((iPM - (channels_1/2)) / 8)

        
        #print(UpDwID,SCID)
        PMinSC = iPM - (SCID * 8 + channels_1/2 * UpDwID)
        fGeoIDs[iPM] = UpDwID * 100000 + SCID * 100 + PMinSC; 

        string = "{}".format(fGeoIDs[iPM])
        out.write(string + '\n')

        ### Needed to create rawDecoder
        if (PMinSC % 8 == 0 and iPM != 0):
            count += 1
            pos_map.append(pos) 
            pos = []

        if (PMinSC % 8 == 0):
            supercell.append(UpDwID * 100000 + SCID * 100 + 1*10)

        if count == 2:
            channel_map.append(channel)
            channel = []
            count = 0

        if PMinSC == 4:
            pos_SC.append([PM_positions[iPM][0]- x_center, PM_positions[iPM][1]-y_Center]) 
            count_sc += 1

        if count_sc == 2:
            pos_map_SC.append(pos_SC)
            pos_SC = []
            count_sc = 0

        #print(PM_positions[iPM][0],PM_positions[iPM][1])
        pos.append([PM_positions[iPM][0]- x_center, PM_positions[iPM][1]-y_Center])
        channel.append(int(fGeoIDs[iPM]))
        
        if iPM == nPM-1:
            channel_map.append(channel)
            pos_map.append(pos)

    #print(fGeoIDs[iPM],DecodeChannelID(fGeoIDs[iPM]))
    #print(DecodeChannelID(fGeoIDs[iPM])[-1]%8)
    #if (iPM == channels_1/2):
    #    break

tmp = []
for p in range(len(supercell)):
    if p%16 == 0 and p !=0:
        supercell_map.append(tmp)
        tmp = []
    
    if p+1 == len(supercell):
        supercell_map.append(tmp)

    tmp.append(supercell[p])


createRawDec = False
list_string = []
print(len(channel_map)) 
print(channel_map[260])
if createRawDec:
    try: 
        os.remove('RawDecoder_{}.txt'.format(SiType)) 
    except FileNotFoundError:
        pass
    with open('RawDecoder_{}.txt'.format(SiType), 'w') as out:
        adder = [0,1000000,]
        adder_i = [0,len(channel_map),len(channel_map)*2+1, len(channel_map)*2+len(supercell_map)+1]
        for v in range(0,4):
            if v<2:
                for i in range(len(channel_map)):
                    substring = ""
                    #print(channel_map[i])
                    for t in range(len(channel_map[i])):
                        substring += " {}".format(channel_map[i][t]+adder[v])
                    string = "ChRemap_{:04n}={}".format(i+adder_i[v],substring)
                    list_string.append(string)
                    out.write(string + '\n')
            else:
                for i in range(len(supercell_map)):
                    substring = ""
                    #print(supercell_map[i])
                    for t in range(len(supercell_map[i])):
                        substring += " {}".format(supercell_map[i][t]+adder[v-2])
                    string = "ChRemap_{:04n}={}".format(len(list_string),substring)
                    list_string.append(string)
                    out.write(string + '\n')


            print(v ,len(list_string) % 32)
            if (v == 1 or v ==3):
                print(v, len(list_string), len(list_string) % 32)
                if (len(list_string) % 32 > 0):
                    q = 0
                    for po in range(32 -(len(list_string) % 32)):
                        print(po,32 -(len(list_string) % 32))
                        substring = ""
                        for t in range(16):
                            substring += " {}".format(-1)
                        string = "ChRemap_{:04n}={}".format(len(list_string),substring)
                        print(len(list_string))
                        list_string.append(string)
                        #print(string)
                        q += 1
                        out.write(string + '\n')
                        if v == 0:
                            adder_i[v+1] += 1
                        if v == 1:
                            adder_i[v+1] += 1
            #else:
                if (len(list_string) % 8 > 0):
                    q = 0
                    for po in range(8-(len(list_string) % 8)):
                        substring = ""
                        for t in range(16):
                            substring += " {}".format(-1)
                        string = "ChRemap_{:04n}={}".format(len(list_string),substring)
                        list_string.append(string)
                        #print(string)
                        q += 1
                        out.write(string + '\n')
                        if v == 0:
                            adder_i[v+1] += 1
                        if v == 1:
                            adder_i[v+1] += 1

            

create_conf = False

if create_conf:
        try: 
            os.remove('PMTPositions_{}.txt'.format(SiType)) 
        except FileNotFoundError:
            pass 
        with open('PMTPositions_{}.dat'.format(SiType), 'w') as out:
            for i in range(len(pos_map)):
                substring = ""
                for t in range(len(pos_map[i])):
                    substring += " {}".format(pos_map[i][t][0])
                    substring += " {}".format(pos_map[i][t][1])
                string = "PMPosition_SC_{} ={}".format(i,substring)
                out.write(string + '\n')


create_SC_pos = False

if create_SC_pos:
        try: 
            os.remove('SCPositions_{}.txt'.format(SiType)) 
        except FileNotFoundError:
            pass 
        with open('SCPositions_{}.dat'.format(SiType), 'w') as out:
            for i in range(len(pos_map_SC)):
                substring = ""
                for t in range(len(pos_map_SC[i])):
                    substring += " {}".format(pos_map_SC[i][t][0])
                    substring += " {}".format(pos_map_SC[i][t][1])
                string = "SCPosition_SC_{} ={}".format(i,substring)
                out.write(string + '\n')

exit(0)
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