#!/usr/bin/env python

inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

sensordata = {}
Xs = []
Ys = []

for line in data_list:
    sensor,beacon = line.split(":")
    sensorx,sensory = sensor.split(",")
    sensorX = int(sensorx.split("=")[-1])
    sensorY = int(sensory.split("=")[-1])
    beaconx,beacony = beacon.split(",")
    beaconX = int(beaconx.split("=")[-1])
    beaconY = int(beacony.split("=")[-1])
    sensordata[(sensorX,sensorY)] = (beaconX,beaconY)
    Xs.append(sensorX)
    Ys.append(sensorY)
    Xs.append(beaconX)
    Ys.append(beaconY)

minX = min(Xs)
minY = min(Ys)
maxX = max(Xs)
maxY = max(Ys)

def printMap():
    lines = []
    for i in range(minY,maxY):
        line = ""
        for j in range(minX,maxX):
            try:
                line += sensorMap[(j,i)]
            except:
                line += "."
        print(line)
        lines.append(line)
    return lines
            


def getManhattanPoints(point,distance):
    print(point,distance)
    points = set()
    for n in range(distance+1):
        for i in range(point[1]-distance+n,point[1]+distance+1-n):
            if i == 2000000:
                points.add((point[0]+n,i))
                points.add((point[0]-n,i))
    print(point,distance,points)
    return points




sensorMap = {}
theRow = []
for sensor in sensordata.keys():
    sensorMap[sensor] = "S"
    beacon = sensordata[sensor]
    sensorMap[beacon] = "B"
    manhattan = abs(beacon[0]-sensor[0]) + abs(beacon[1]-sensor[1])
    Xs.append(sensor[0]-manhattan)
    Xs.append(sensor[0]+manhattan+1)
    Ys.append(sensor[1]-manhattan)
    Ys.append(sensor[1]+manhattan+1)
    # print(sensor, manhattan)
    if sensor[1] <= 2000000 and (sensor[1] + manhattan) >= 2000000:
        print(sensor, manhattan)
        count = 0
        for i in range(2000000,sensor[1]+manhattan):
            count += 1
        for i in range(sensor[0]-count,sensor[0]+count+1):
            if not (i,2000000) in sensorMap.keys():
                sensorMap[(i,2000000)] = "#"

    elif sensor[1] >= 2000000 and (sensor[1] - manhattan) <= 2000000:
        print(sensor, manhattan)
        count = 0
        for i in range(sensor[1]-manhattan, 2000000):
            count += 1
        for i in range(sensor[0]-count,sensor[0]+count+1):
            if not (i,2000000) in sensorMap.keys():
                sensorMap[(i,2000000)] = "#"

        # points = getManhattanPoints(sensor,manhattan)
        # for point in points:
        #     if not point in sensorMap.keys():
        #         sensorMap[point] = "#"
            


minX = min(Xs)
minY = min(Ys)
maxX = max(Xs)
maxY = max(Ys)

# themap = printMap()
# print(themap[2000000+abs(minY)])
# chars = 0
# for char in themap[2000000+abs(minY)]:
#     if char == "#":
#         chars += 1

# print(chars)

chars = 0
for key in sensorMap.keys():
    if key[1] == 2000000 and sensorMap[key] != "S" and sensorMap[key] != "B":
        chars += 1

print(chars)