import numpy as np

fGigaTrackerActiveSensorLength = [60.8 , 27.0 , 0.2]

fGigaTrackerSmallPixelLength = [[300.0e-3, 300.0e-3, 200.0e-3], [150.0e-3, 150.0e-3, 200.0e-3], [100.0e-3, 100.0e-3, 200.0e-3]]  #mm
fGigaTrackerBigPixelLength = [[400.0e-3, 300.0e-3, 200.0e-3]] #mm

def GetNCols(PixelType):
    NCols_mBig = (fGigaTrackerActiveSensorLength[0] - (10 * fGigaTrackerBigPixelLength[0][0])) / fGigaTrackerSmallPixelLength[PixelType][0]

    NTCols = np.ceil(NCols_mBig + 10)

    return NTCols

def GetNRows(PixelType):

    NTRows = np.ceil(fGigaTrackerActiveSensorLength[1]/fGigaTrackerSmallPixelLength[PixelType][1])/2

    return NTRows

pos = [[]]*18000


with open('gtkpos.txt') as f:
    for ln in f:
        token = ln.strip("\n").split(" ")
        id = int(token[0])
        x = float(token[1])
        y = float(token[2])
        print(id)
        pos[id] = [x,y]