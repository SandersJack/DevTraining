import numpy as np
import matplotlib.pyplot as plt

fPixelType = 1

fGigaTrackerSensorLength = [63.1, 29.3, 0.2]
fGigaTrackerActiveSensorLength = [60.8 , 27.0 , 0.2]


fGigaTrackerSmallPixelLength = [[300.0e-3, 300.0e-3, 200.0e-3], [150.0e-3, 150.0e-3, 200.0e-3], [100.0e-3, 100.0e-3, 200.0e-3]]  #mm
fGigaTrackerBigPixelLength = [[400.0e-3, 300.0e-3, 200.0e-3],[250.0e-3, 150.0e-3, 200.0e-3],[200.0e-3, 100.0e-3, 200.0e-3]] #mm

def GetNCols(PixelType):
    NCols_mBig = (fGigaTrackerActiveSensorLength[0] - (10 * fGigaTrackerBigPixelLength[PixelType][0])) / fGigaTrackerSmallPixelLength[PixelType][0]

    NTCols = np.ceil(NCols_mBig + 10)

    return (NTCols)

def GetNRows(PixelType):

    NTRows = np.ceil(fGigaTrackerActiveSensorLength[1]/fGigaTrackerSmallPixelLength[PixelType][1])/2

    return (NTRows)


fGigaTrackerNChips = 10
fGigaTrackerChipNColumns = int((GetNCols(fPixelType))/(fGigaTrackerNChips/2))
fGigaTrackerChipNRows = int((GetNRows(fPixelType)))
print(fGigaTrackerChipNColumns,fGigaTrackerChipNRows)

fGigaTrackerSensorNColumns = int(0.5 * fGigaTrackerNChips * fGigaTrackerChipNColumns)

def GetGigaTrackerNumberOfPixels():
  return fGigaTrackerNChips * fGigaTrackerChipNColumns * fGigaTrackerChipNRows;


def GetGigaTrackerActiveSensorXLength():
  return fGigaTrackerActiveSensorLength[0]

def GetGigaTrackerActiveSensorYLength():
  return fGigaTrackerActiveSensorLength[1]

def GetGigaTrackerActiveSensorZLength():
  return fGigaTrackerActiveSensorLength[2]


def PixelXOffset(id):
  N = np.floor(id / fGigaTrackerSensorNColumns) * fGigaTrackerSensorNColumns
  Xindex = int(id - N)
  #print(Xindex, id, N)
  # N_big_*: # big pixels *before* pixel <id>
  N_big_1 = int((Xindex - 1) / fGigaTrackerChipNColumns)  #// 41/81/121/161
  N_big_2 = int(Xindex / fGigaTrackerChipNColumns)     #// 40/80/120/160
  #print((Xindex - N_big_1 - N_big_2) * fGigaTrackerSmallPixelLength[0] + (N_big_1 + N_big_2) * fGigaTrackerBigPixelLength[0])
  #print(fGigaTrackerSmallPixelLength[fPixelType][0])
  return (Xindex - N_big_1 - N_big_2) * fGigaTrackerSmallPixelLength[fPixelType][0] + (N_big_1 + N_big_2) * fGigaTrackerBigPixelLength[fPixelType][0]


def PixelIsBig(id):
    N = int(id / fGigaTrackerSensorNColumns) * fGigaTrackerSensorNColumns
    Xindex = int(id - N)
    # 40 / 80 / 120 / 160
    if(Xindex % int(fGigaTrackerChipNColumns) == 0 and Xindex != 0):
        return True
    # 39 / 79 / 119 / 159
    if((Xindex + 1) % int(fGigaTrackerChipNColumns) == 0 and Xindex != int(fGigaTrackerSensorNColumns - 1)):
        return True
    return False

def GetPixelXPosition(id):
  if(PixelIsBig(id)):
    return PixelXOffset(id) + 0.5 * fGigaTrackerBigPixelLength[fPixelType][0]
  else:
    return PixelXOffset(id) + 0.5 * fGigaTrackerSmallPixelLength[fPixelType][0]


def GetPixelYPosition(id):
  return 0.5 * fGigaTrackerSmallPixelLength[fPixelType][1] + int(id / fGigaTrackerSensorNColumns) * fGigaTrackerSmallPixelLength[fPixelType][1]


def GetPixelXLength(id):
  if(PixelIsBig(id)):
    return fGigaTrackerBigPixelLength[fPixelType][0]
  return fGigaTrackerSmallPixelLength[fPixelType][0]

def GetPixelYLength(G4int):
    return fGigaTrackerSmallPixelLength[fPixelType][1]


Ncopys = GetGigaTrackerNumberOfPixels()

animate = False

if animate:
    fig = plt.figure(figsize=(5,5))

    plt.xlim(-35,35)
    plt.ylim(-20,20)

def plot(x,y,id):
    if animate:
        #print(k,l,m,n)
        if id%2 == 0:
            col = "red"
        else:
            col = "green"
        #circle = plt.Circle((x-x_center,y-y_center),7.5, fc=col,ec="blue")
        print(i,GetPixelXLength(id))
        rectangle1 = plt.Rectangle((x,y), GetPixelXLength(id)/2, GetPixelYLength(id)/2, fc=col)
        rectangle2 = plt.Rectangle((x,y), GetPixelXLength(id)/2, -GetPixelYLength(id)/2, fc=col)
        rectangle3 = plt.Rectangle((x,y), -GetPixelXLength(id)/2, GetPixelYLength(id)/2, fc=col)
        rectangle4 = plt.Rectangle((x,y), -GetPixelXLength(id)/2, -GetPixelYLength(id)/2, fc=col)
        #plt.plot(x,y)
        plt.gca().add_patch(rectangle1)
        plt.gca().add_patch(rectangle2)
        plt.gca().add_patch(rectangle3)
        plt.gca().add_patch(rectangle4)
        plt.pause(0.001)
        if id == 0:
            pass
        else:
            plt.draw()

pos = []
print(Ncopys)

testing = False

if testing:
  pos_frame = [[]]*18000
  with open('gtkpos.txt') as f:
    for ln in f:
        token = ln.strip("\n").split(" ")
        id = int(token[0])
        x = float(token[1])
        y = float(token[2])
        #print(id)
        pos_frame[id] = [x,y]


for i in range(int(Ncopys)):
  X = GetPixelXPosition(i) - 0.5 * GetGigaTrackerActiveSensorXLength()
  Y = GetPixelYPosition(i) - 0.5 * GetGigaTrackerActiveSensorYLength()
  Z = 0
  if (testing):
    if(pos_frame[i][0] != round(X*100)/100):
      print(X,pos_frame[i][0])
      exit(0)
  pos.append([X,Y,Z])
  plot(X,Y,i)
  print(i,X,Y)
    
exit(0)

if not animate:
    print("No Animate")
    fig = plt.figure(figsize=(20,20))
    plt.xlim(-50,50)
    plt.ylim(-50,50)
    col = 'red'
    for i in range(len(pos)):
        

        
        #print(PM_positions[i][0],PM_positions[i][1])
        #print(GetPixelXLength(i),round(i%fGigaTrackerChipNColumns) )
        #if (i != 0 and round(i%fGigaTrackerChipNColumns) ==0):
        #  exit(0)


        rectangle1 = plt.Rectangle((pos[i][0],pos[i][1]), GetPixelXLength(i)/2, GetPixelYLength(i)/2, fc=col)
        rectangle2 = plt.Rectangle((pos[i][0],pos[i][1]), GetPixelXLength(i)/2, -GetPixelYLength(i)/2, fc=col)
        rectangle3 = plt.Rectangle((pos[i][0],pos[i][1]), -GetPixelXLength(i)/2, GetPixelYLength(i)/2, fc=col)
        rectangle4 = plt.Rectangle((pos[i][0],pos[i][1]), -GetPixelXLength(i)/2, -GetPixelYLength(i)/2, fc=col,)
        #plt.plot(x,y)
        plt.gca().add_patch(rectangle1)
        plt.gca().add_patch(rectangle2)
        plt.gca().add_patch(rectangle3)
        plt.gca().add_patch(rectangle4)

        if (((i)%2 == 0 and i%fGigaTrackerChipNColumns*5 != 0)):
            #print(i)
            if col == 'red':
                col='green'
            else:
                col='red'

plt.savefig('GTK_{}.png'.format(fPixelType))
plt.show()