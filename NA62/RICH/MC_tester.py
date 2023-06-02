import uproot
import matplotlib.pyplot as plt

NChannels = 18684
nChannelsDiff = NChannels - 2076

def GeoToSeq(GeoID):
    NChannels = nChannelsDiff/2
    NSC = int((NChannels*2)/8)
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

filename = "PMTPositons_1.dat"

n = 0


fPMsPositions = [[0 for i in range(2)] for i in range(NChannels)]

for line in open(filename):
    listWords = line.strip("\n").split(" ")
    #print(listWords)
    for i in range(8):
        x = listWords[2*i + 2]
        y = listWords[2*i + 3]

        fPMsPositions[8*n + i][0] = float(x)
        fPMsPositions[8*n + i][1] = float(y)
        fPMsPositions[int(8*n + i + nChannelsDiff/2)][0] = float(x)
        fPMsPositions[int(8*n + i + nChannelsDiff/2)][1] = float(y)
        #print(8*n + i,fPMsPositions[8*n + i])
        #print(int(8*n + i + nChannelsDiff/2),fPMsPositions[int(8*n + i + nChannelsDiff/2)])

    #if n == 10:
    #    exit(0)
    n += 1
if False:
    l = 0
    for line in open("Channels_1.txt"):
        ch_id = int(float(line.strip("\n"))) 
        print(ch_id, GeoToSeq(ch_id), fPMsPositions[GeoToSeq(ch_id)])
        if l == 600:
            break
        l += 1

file = uproot.open("pluto._dr020000_r000000.root")

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
            hitpos_salev_x.append(fPMsPositions[GeoToSeq(channels[t][p])][0])
            hitpos_salev_y.append(fPMsPositions[GeoToSeq(channels[t][p])][1])
            
fig, ax = plt.subplots(figsize=(10,10))

ax.hist2d(hitpos_jura_x,hitpos_jura_y, bins=(100,100), range=[[-300,300],[-300,300]])

fig1, ax1 = plt.subplots(figsize=(10,10))

ax1.hist2d(hitpos_salev_x,hitpos_salev_y, bins=(100,100), range=[[-300,300],[-300,300]])
plt.show()