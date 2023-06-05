
fGigaTrackerSmallPixelLength = [300.0e-3, 300.0e-3, 200.0e-3] #mm
fGigaTrackerBigPixelLength = [400.0e-3, 300.0e-3, 200.0e-3] #mm

fGigaTrackerSensorLength = [63.1, 29.3, 0.2]
fGigaTrackerActiveSensorLength = [60.8 , 27.0 , 0.2]

fGigaTrackerNChips = 10
fGigaTrackerChipNColumns = 40
fGigaTrackerChipNRows = 45

fGigaTrackerSensorNColumns = 0.5 * fGigaTrackerNChips * fGigaTrackerChipNColumns

def GetGigaTrackerNumberOfPixels():
  return fGigaTrackerNChips * fGigaTrackerChipNColumns * fGigaTrackerChipNRows;


def GetGigaTrackerActiveSensorXLength():
  return fGigaTrackerActiveSensorLength[0]

def GetGigaTrackerActiveSensorYLength():
  return fGigaTrackerActiveSensorLength[1]

def GetGigaTrackerActiveSensorZLength():
  return fGigaTrackerActiveSensorLength[2]


def PixelXOffset(id):
  N = (id / fGigaTrackerSensorNColumns) * fGigaTrackerSensorNColumns;
  Xindex = (id - N)
  # N_big_*: # big pixels *before* pixel <id>
  N_big_1 = (Xindex - 1) / fGigaTrackerChipNColumns;  #// 41/81/121/161
  N_big_2 = Xindex / fGigaTrackerChipNColumns;        #// 40/80/120/160
  return (Xindex - N_big_1 - N_big_2) * fGigaTrackerSmallPixelLength[0] + (N_big_1 + N_big_2) * fGigaTrackerBigPixelLength[0];


def PixelIsBig(id):
    N = (id / fGigaTrackerSensorNColumns) * fGigaTrackerSensorNColumns
    Xindex = (id - N)
    # 40 / 80 / 120 / 160
    if(Xindex % fGigaTrackerChipNColumns == 0 and Xindex != 0):
        return True
    # 39 / 79 / 119 / 159
    if((Xindex + 1) % fGigaTrackerChipNColumns == 0 and Xindex != (fGigaTrackerSensorNColumns - 1)):
        return True
    return False

def GetPixelXPosition(id):
  if(PixelIsBig(id)):
    return PixelXOffset(id) + 0.5 * fGigaTrackerBigPixelLength[0]
  else:
    return PixelXOffset(id) + 0.5 * fGigaTrackerSmallPixelLength[0]


def GetPixelYPosition(id):
  return 0.5 * fGigaTrackerSmallPixelLength[1] + (id / fGigaTrackerSensorNColumns) * fGigaTrackerSmallPixelLength[1]


def GetPixelXLength(id):
  if(PixelIsBig(id)):
    return fGigaTrackerBigPixelLength[0]
  return fGigaTrackerSmallPixelLength[0]

def GetPixelYLength(G4int):
    return fGigaTrackerSmallPixelLength[1]


Ncopys = GetGigaTrackerNumberOfPixels()


for i in range(Ncopys):
  X = GetPixelXPosition(i) - 0.5 * GetGigaTrackerActiveSensorXLength()
  Y = GetPixelYPosition(i) - 0.5 * GetGigaTrackerActiveSensorYLength()
  Z = 0
  print(i,X,Y)