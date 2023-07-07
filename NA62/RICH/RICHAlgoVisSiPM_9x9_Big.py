import numpy as np
import matplotlib.pyplot as plt
import os

m = 1000
mm = 1


def DecodeChannelID(ChannelID):
    DiskID = np.floor(ChannelID / 100000)
    UpDownDiskID = np.floor((ChannelID % 100000) / 10000)
    SuperCellID = np.floor((ChannelID % 10000) / 10)
    OrSuperCellID = np.floor((ChannelID % 100) / 10)
    PmtID = np.floor(ChannelID % 10)
    
    return DiskID,UpDownDiskID,SuperCellID,OrSuperCellID,PmtID

SiType = 1 # 0 = 3mm, 1 = 6mm, 2 = 9mm

SpotHeight = 0.30 * m
SpotWidth = 0.325 * m
SpotRadius = 0.3 * m

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
    nRow = 23
    channels_1 = 10#int(8304*3)
    id_length = 301
elif SiType == 2:
    SensorWidth = 0.009 * m
    cen_fac = 18/9
    supercell_fac = 25
    nRow = 12
    channels_1 = 3816
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
x_center = 0#285
y_center = 0


if animate:
    fig = plt.figure(figsize=(5,5))

    plt.xlim(-400,400)
    plt.ylim(-400,400)

    

    #circle = plt.Circle((0,0),SpotRadius, fc="white",ec="blue")
    square1 = plt.Rectangle((-SpotWidth,-SpotHeight),SpotWidth, SpotHeight, fc="white",ec="blue" )
    #plt.gca().add_patch(circle)
    
def plot(x,y,n,m,l,k,i):
    if animate:
        #x_center = 0
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

    
large_radius = 2130               

small_radius = 1220


for k in range(nRow):
    break
      #first half
    nSuperCellinRow[k] = 0
    x_width = np.sqrt(large_radius**2 - ((k)*3*SensorWidth)**2)

    x_width_2 = x_width-np.sqrt(small_radius**2 - ((k)*3*SensorWidth)**2)

    if small_radius < (k)*3*SensorWidth/0.1989:
        x_width_2 = x_width-(((k)*3*SensorWidth)/(0.1989*0.99))

    #print(((k)*3*SensorWidth),small_radius,((k)*3*SensorWidth)/0.1989,x_width, x_width_2)
    
    while((nSuperCellinRow[k] + 1) * SensorWidth * 3/3 < x_width_2+(SensorWidth)):
        nSuperCellinRow[k] +=1
    nSuperCellinRow[k] +=1
    
    if(k != 0):
        cell_dist[k] = int(np.floor((large_radius-x_width) / (SensorWidth)))

    if(k == 0):
        x_center = 600 - (nSuperCellinRow[k]) * SensorWidth * 3/3 /2 -10 
        #print(x_center)
    
    triCell = 0 
    if k%2 == 0:
        for l in range(nSuperCellinRow[k]):
            for m in range(0,3):
                PM_positions[nPM][0] = (-1 + l + cell_dist[k])*SensorWidth
                PM_positions[nPM][1] = (m + k*3 + 0.5)*SensorWidth; #SensorWidth*m + SensorWidth*k*3
                #fPMsIDs[-1 + l + cell_dist[k]][m + k*3] = nPM;
                #print(l)
                #print(-1 + l + cell_dist[k],m + k*3)
                plot(PM_positions[nPM][0],PM_positions[nPM][1],-1,m,l,k,nPM)
                #print(PM_positions[nPM][0],PM_positions[nPM][1])
                nPM += 1
                if nPM ==1:
                    x_center = PM_positions[nPM-1][0] + large_radius
        #exit(l)
                
    else:
        for l in range(nSuperCellinRow[k],0,-1):
            for m in range(0,3):
                PM_positions[nPM][0] = (l + cell_dist[k]-2)*SensorWidth
                PM_positions[nPM][1] = (m + k*3 + 0.5)*SensorWidth; #SensorWidth*m + SensorWidth*k*3
                #fPMsIDs[l + cell_dist[k]-2][m + k*3] = nPM;
                #print(-2 + l + cell_dist[k],m + k*3)
                plot(PM_positions[nPM][0],PM_positions[nPM][1],-1,m,l,k,nPM)
                #print(PM_positions[nPM][0],PM_positions[nPM][1])
                #exit(0)
                nPM += 1
                if nPM ==1:
                    x_center = PM_positions[nPM-1][0] + 300
            #print(triCell) 
    #print(PM_positions[0][0],PM_positions[0][1])
#end first half

for j in range(nRow): 
    break
    triCell = 0
    if j%2 == 0:
        for l in range(nSuperCellinRow[j]):
            for m in range(0,3):
                PM_positions[nPM][0] = (-1 + l + cell_dist[j])*SensorWidth;
                                
                PM_positions[nPM][1] = -(m + j*3 + 0.5)*SensorWidth; #SensorWidth*m + SensorWidth*k*3
                
                #fPMsIDs[-1 + l + cell_dist[j]+ 200][m + j*3 + 200] = nPM;
                #print(l + cell_dist[j] - 1 + 200,m + j*3 + 200)
                #plot(PM_positions[nPM][0],PM_positions[nPM][1],-1,m,l,k,nPM)
                nPM += 1
                #print(n + l*3 + 3*cell_dist[j] - triCell+ 300)
                
    else:
        for l in range(nSuperCellinRow[j],0,-1):
            for m in range(0,3):
               
                PM_positions[nPM][0] = (l + cell_dist[j]-2)*SensorWidth;       
                PM_positions[nPM][1] = -(m + j*3 + 0.5)*SensorWidth; #SensorWidth*m + SensorWidth*k*3
                
                #fPMsIDs[l + cell_dist[j] - 2 + 200][m + j*3 + 200] = nPM;
                #print(l + cell_dist[j] - 2 + 200,m + j*3 + 200)
                #plot(PM_positions[nPM][0],PM_positions[nPM][1],-1,m,l,k,nPM)
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
        if (SiType == 1 or SiType == 2):
            fGeoIDs[iPM] = UpDwID * 100000 + SCID * 100 + PMinSC; # For type 0 need to change this
        else:
            fGeoIDs[iPM] = UpDwID * 1000000 + SCID * 100 + PMinSC;

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

        if (SCID % 3 == 0 and PMinSC % 8 == 4) or (SCID % 3 == 2 and PMinSC % 8 == 3) or (SCID % 3 == 1 and PMinSC % 8 == 5):
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
            pos_map_SC.append(pos_SC)

    #print(fGeoIDs[iPM],DecodeChannelID(fGeoIDs[iPM]))
    #print(DecodeChannelID(fGeoIDs[iPM])[-1]%8)
    #if (iPM == channels_1/2):
    #    break

neighbours = False

if neighbours:
    try: 
        os.remove('RICH-PMsNeighboursMap_{}.txt'.format(SiType)) 
    except FileNotFoundError:
        pass
    with open('RICH-PMsNeighboursMap_{}.txt'.format(SiType), 'w') as out:
        for disk in range(2):
            shift = len(fGeoIDs)
            channel_shift = 10000000
            for i in range(len(fGeoIDs)):
                secID = fGeoIDs[i]
                pos_x = PM_positions[i][0]- x_center
                pos_y = PM_positions[i][1]- y_Center

                neighbours = [-99,-99,-99,-99]
                neigh = 0
                for t in range(len(fGeoIDs)):
                    pos_x_chec = PM_positions[t][0]- x_center
                    pos_y_chec = PM_positions[t][1]- y_Center
                    if (abs(pos_x_chec - pos_x) <= SensorWidth and abs(pos_y_chec - pos_y) <= SensorWidth) and t != i and (abs(pos_x_chec - pos_x) != abs(pos_y_chec - pos_y)):
                        if disk == 0:
                            neighbours[neigh] = int(fGeoIDs[t])
                        else:
                            neighbours[neigh] = int(fGeoIDs[t] + channel_shift)
                        neigh += 1

                if disk == 0:
                    string_ = "{} ".format(i)
                else:
                    string_ = "{} ".format(i+shift)

                for u in range(len(neighbours)):
                    string_ += "{} ".format(neighbours[u])

                out.write(string_ + '\n')


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
chun = 0
n = 0
#print(len(channel_map)) 
#for i in range(len(channel_map)):
#    for t in range(len(channel_map[i])):
#        print(n + t,channel_map[i][t] )
#    n += len(channel_map[i])

#print(chun)
if createRawDec:
    try: 
        os.remove('RawDecoder_{}.txt'.format(SiType)) 
    except FileNotFoundError:
        pass
    with open('RawDecoder_{}.txt'.format(SiType), 'w') as out:
        if (SiType == 1 or SiType == 2):
            adder = [0,1000000,]
        else:
            adder = [0,10000000,]
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


            #print(v ,len(list_string) % 32)
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
                print(len(pos_map[i]) % 8)
                if len(pos_map[i]) % 8 != 0:
                    for add in range(8 - len(pos_map[i]) % 8):
                        pos_map[i].append([-999.0, -999.0])
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
                    plot(pos_map_SC[i][t][0],pos_map_SC[i][t][1],-1,0,i,0,0)
                    substring += " {}".format(pos_map_SC[i][t][0])
                    substring += " {}".format(pos_map_SC[i][t][1])
                string = "SCPosition_SC_{} ={}".format(i,substring)
                out.write(string + '\n')

#print(fPMsIDs)

def plotinit():
    fig = plt.figure(figsize=(10,10))
    #plt.xlim(-1000,1000)
    #plt.ylim(-1000,1000)
    r = 2150
    arc_angles = np.linspace(-np.pi/14 + np.pi , np.pi+ np.pi/14, 1000)
    arc_xs = r * np.cos(arc_angles)
    arc_ys = r * np.sin(arc_angles)
    plt.plot(arc_xs, arc_ys, color = 'red', lw = 3)

    r2 = 1200
    arc_angles2 = np.linspace(-np.pi/14 + np.pi , np.pi+ np.pi/14, 1000)
    arc_xs2 = r2 * np.cos(arc_angles) 
    arc_ys2 = r2 * np.sin(arc_angles)
    plt.plot(arc_xs2, arc_ys2, color = 'red', lw = 3)

    posx = r * np.cos(np.pi+ np.pi/16)
    posy =  r * np.sin(np.pi+ np.pi/16)

    posx_in = r2 * np.cos(np.pi+ np.pi/16)
    posy_in =  r2 * np.sin(np.pi+ np.pi/16)

    points_x = [posx_in,posx]
    points_y = [posy_in,posy]

    plt.plot(points_x,points_y, "b--")

    posx_2 = r * np.cos(np.pi+ -np.pi/16)
    posy_2 =  r * np.sin(np.pi+ -np.pi/16)

    posx_in_2 = r2 * np.cos(np.pi+ -np.pi/16)
    posy_in_2 =  r2 * np.sin(np.pi+ -np.pi/16)

    points_x_2 = [posx_in_2,posx_2]
    points_y_2 = [posy_in_2,posy_2]

    plt.plot(points_x_2,points_y_2, "b--")

    posx_3 = r * np.cos(np.pi+ -np.pi/14)
    posy_3 =  r * np.sin(np.pi+ -np.pi/14)

    posx_in_3 = r2 * np.cos(np.pi+ -np.pi/14)
    posy_in_3 =  r2 * np.sin(np.pi+ -np.pi/14)

    points_x_3 = [posx_in_3,posx_3]
    points_y_3 = [posy_in_3,posy_3]

    plt.plot(points_x_3,points_y_3, "r")

    posx_4 = r * np.cos(np.pi+ np.pi/14)
    posy_4 =  r * np.sin(np.pi+ np.pi/14)

    posx_in_4 = r2 * np.cos(np.pi+ np.pi/14)
    posy_in_4 =  r2 * np.sin(np.pi+ np.pi/14)

    points_x_4 = [posx_in_4,posx_4]
    points_y_4 = [posy_in_4,posy_4]

    plt.plot(points_x_4,points_y_4, "r")

    


#x_center = 297
y_center = 0
ang = 0
print(nPM)
if not animate:
    print("No Animate")
    
    plotinit()
    circle = plt.Circle((-1600,0),SpotRadius, fc="white",ec="blue",alpha=0.5)
    square1 = plt.Rectangle((-SpotWidth-1600,-SpotHeight),SpotWidth*2, SpotHeight*2, fc="white",ec="blue" )
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


plt.gca().add_patch(square1)
plt.gca().add_patch(circle)
plt.xlim(-2200, -1000)
#plt.savefig('SiPM_new_{}.png'.format(SiType))
plt.show()