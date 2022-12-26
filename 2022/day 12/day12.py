#!/usr/bin/env python
from math import *

inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

theMap = {}
for y in range(len(data_list)):
    for x in range(len(data_list[y])):
        theMap[(x,y)] = data_list[y][x]

theMapLength = len(data_list[0])
theMapHeight = len(data_list)
# print(theMap)

end = next(k for k,v in theMap.items() if v == "S")
theMap[end] = "a"

start = next(k for k,v in theMap.items() if v == "E")
theMap[start] = "z"

current = start
steps = [start]
while current != end:
    # add neighbors to candidate list
    x = current[0]
    y = current[1]
    candidates = []
    # print(x,y)
    # print(ord(theMap[(x,y)]))
    if x - 1 > -1:
        # print(ord(theMap[(x-1,y)]))
        if (x-1,y) not in steps \
            and ord(theMap[(x-1,y)]) <= ord(theMap[current])+1 \
                and ord(theMap[(x-1,y)]) >= ord(theMap[current])-1 :
            candidates.append((x-1,y))
    if x + 1 < theMapLength:
        # print(ord(theMap[(x+1,y)]))
        if (x+1,y) not in steps \
            and ord(theMap[(x+1,y)]) <= ord(theMap[current])+1 \
                and ord(theMap[(x+1,y)]) >= ord(theMap[current])-1:
            candidates.append((x+1,y))
    if y - 1 > -1:
        # print(ord(theMap[current]),ord(theMap[(x,y-1)]))
        if (x,y-1) not in steps \
            and ord(theMap[(x,y-1)]) <= ord(theMap[current])+1 \
                and ord(theMap[(x,y-1)]) >= ord(theMap[current])-1:
            candidates.append((x,y-1))
    if y + 1 < theMapHeight:
        # print(ord(theMap[(x,y+1)]))
        if (x,y+1) not in steps \
            and ord(theMap[(x,y+1)]) <= ord(theMap[current])+1 \
                and ord(theMap[(x,y+1)]) >= ord(theMap[current])-1:
            candidates.append((x,y+1))


    print(candidates)
    if not candidates:
        print("no suitable moves found")
        print("current: (",x,",",y,")")
        print("steps:",steps)
        exit()
    distances = {}
    for point in candidates:
        distances[point] = sqrt((end[0] - point[0])**2 + (end[1] - point[1])**2)

    weight = 100
    for distance in distances.values():
        if distance < weight:
            weight = distance
    # print(weight)
    # print(distances)
    chosen = list(distances.keys())[list(distances.values()).index(weight)]
    steps.append(chosen)
    current = chosen

print("steps:", len(steps)-1,"-",steps)


