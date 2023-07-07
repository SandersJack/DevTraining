import uproot
import matplotlib.pyplot as plt

animate = False
SensorWidth = 9

if animate:
    fig = plt.figure(figsize=(5,5))

    plt.xlim(-300,300)
    plt.ylim(-300,300)

def plot(x,y):
    if animate:
        #print(k,l,m,n)
        shiftx = 1
        shifty = 1
        if l%2 == 0:
            col = "red"
        else:
            col = "green"
        #circle = plt.Circle((x-x_center,y-y_center),7.5, fc=col,ec="blue")
        rectangle1 = plt.Rectangle((x,y), SensorWidth/2, SensorWidth/2, fc=col)
        rectangle2 = plt.Rectangle((x,y), SensorWidth/2, -SensorWidth/2, fc=col)
        rectangle3 = plt.Rectangle((x,y), -SensorWidth/2, SensorWidth/2, fc=col)
        rectangle4 = plt.Rectangle((x,y), -SensorWidth/2, -SensorWidth/2, fc=col)
        #plt.plot(x,y)
        plt.gca().add_patch(rectangle1)
        plt.gca().add_patch(rectangle2)
        plt.gca().add_patch(rectangle3)
        plt.gca().add_patch(rectangle4)
        plt.pause(0.0001)
        #if plo == 0:
        #    pass
        #else:
        #    pass
            #plt.draw()

itype = 2

if (itype == 1):
    NChannels = 18684
    nChannelsDiff = NChannels - 2076
elif (itype == 2):
    NChannels = 8588
    nChannelsDiff = NChannels - 956
    NSC_ = 956


def GeoToSeq(GeoID):
    NChannels = nChannelsDiff/2
    NSC = int(NSC_)
    DiskID = int(GeoID / 1000000)
    UpDwID = int((GeoID - 1000000 * DiskID) / 100000)
    SCID = int((GeoID - 1000000 * DiskID - 100000 * UpDwID) / 100)
    OrID = int((GeoID - 1000000 * DiskID - 100000 * UpDwID - SCID * 100) / 10)
    PMID = int(GeoID - 1000000 * DiskID - 100000 * UpDwID - SCID * 100 - OrID * 10)

    if(OrID < 1):
      SeqID = int(SCID * 8 + PMID + UpDwID * NChannels/2 + DiskID * NChannels)
    else:
      SeqID = int(NChannels/2 * 2 * 2 + SCID + UpDwID * NSC/4 + DiskID * NSC/2)
    return SeqID

filename = "PMTPositions_2.dat"

n = 0


fPMsPositions = [[0 for i in range(2)] for i in range(NChannels)]

for line in open(filename):
    listWords = line.strip("\n").split(" ")
    #print(listWords)
    pm_insc = 0
    for i in range(8):
        x = listWords[2*i + 2]
        y = listWords[2*i + 3]

        if(float(x) == -999.0 and float(y) == -999.0):
            continue

        fPMsPositions[n + pm_insc][0] = float(x)
        fPMsPositions[n + pm_insc][1] = float(y)
        fPMsPositions[int(n + pm_insc + nChannelsDiff/2)][0] = float(x)
        fPMsPositions[int(n + pm_insc + nChannelsDiff/2)][1] = float(y)
        pm_insc += 1
        #print(8*n + i,fPMsPositions[8*n + i])
        #print(int(8*n + i + nChannelsDiff/2),fPMsPositions[int(8*n + i + nChannelsDiff/2)])

    #if n == 10:
    #    exit(0)
    n += pm_insc
if True:
    l = 0
    for line in open("Channels_2.txt"):
        ch_id = int(float(line.strip("\n"))) 
        print(ch_id, GeoToSeq(ch_id), fPMsPositions[GeoToSeq(ch_id)])
        plot(fPMsPositions[GeoToSeq(ch_id)][0],fPMsPositions[GeoToSeq(ch_id)][1])
        if l == nChannelsDiff/4 +300:
            break
        l += 1
#exit(0)
#for i in range(NChannels):
#    print(i, fPMsPositions[i] )
#    if i == nChannelsDiff/4 +100:
file = uproot.open("pluto._dr020001_r000000.root")

channels = file['SlimMC']['RICH/TDetectorVEvent/fHits.fChannelID'].array()

print(channels)

hitpos_jura_x = []
hitpos_jura_y = []

hitpos_salev_x = []
hitpos_salev_y = []

for t in range(len(channels)):
    for p in range(len(channels[t])):
        #print(channels[t][p], GeoToSeq(channels[t][p]))
        #print(fPMsPositions[GeoToSeq(channels[t][p])])
        if (channels[t][p] > 999999):
            hitpos_jura_x.append(fPMsPositions[GeoToSeq(channels[t][p])][0])
            hitpos_jura_y.append(fPMsPositions[GeoToSeq(channels[t][p])][1])
        else:
            #print(channels[t][p], GeoToSeq(channels[t][p]), fPMsPositions[GeoToSeq(channels[t][p])])
            hitpos_salev_x.append(fPMsPositions[GeoToSeq(channels[t][p])][0])
            hitpos_salev_y.append(fPMsPositions[GeoToSeq(channels[t][p])][1])
            
fig, ax = plt.subplots(figsize=(10,10))

if itype == 1:
    bin_ = (100,100)
elif itype == 2:
    bin_ = (67,67)


ax.hist2d(hitpos_jura_x,hitpos_jura_y, bins=bin_, range=[[-300,300],[-300,300]])

fig1, ax1 = plt.subplots(figsize=(10,10))

ax1.hist2d(hitpos_salev_x,hitpos_salev_y, bins=bin_, range=[[-300,300],[-300,300]])
plt.show()