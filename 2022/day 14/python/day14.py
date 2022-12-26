#!/usr/bin/env python

inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

cave = {}
Xs = []
Ys = []
originals = []


def build_cave(data):
    for line in data:
        points = line.split("->")
        i = 0
        xs = []
        ys = []
        for point in points:
            x = int(point.split(",")[0])
            y = int(point.split(",")[1])
            xs.append(x)
            ys.append(y)
            Xs.append(x)
            Ys.append(y)
            cave[(x,y)] = "#"
            originals.append((x,y))
            if i > 0:
                # print("xs:", xs[i], xs[i-1])
                # print("ys:", ys[i], ys[i-1])
                if xs[i] == xs[i-1]: # if xs are equal, iterate over ys
                    j = xs[i]
                    if ys[i] > ys[i-1]:
                        start = ys[i-1]
                        stop = ys[i]
                    else:
                        start = ys[i]
                        stop = ys[i-1]
                    for k in range(start,stop):
                        cave[(j,k)] = "#"
                if ys[i] == ys[i-1]: # if ys are equal, iterate over xs
                    k = ys[i]
                    if xs[i] > xs[i-1]: # if new one is bigger
                        start = xs[i-1] # start at last one
                        stop = xs[i]+1  # iterate to new one included
                    else:               # if old one is bigger
                        start = xs[i]   # start at new one
                        stop = xs[i-1]+1 # iterate to old one included
                    for j in range(start,stop):
                        cave[(j,k)] = "#"
            i += 1

build_cave(data_list)

minX = min(Xs) - 1
minY = 0
maxX = max(Xs) + 1
maxY = max(Ys) + 2

data_list.append("0,"+str(maxY)+" -> 1000,"+str(maxY))

build_cave(data_list)

minX = min(Xs) - 1
minY = 0
maxX = max(Xs) + 1
maxY = max(Ys) + 2

# line = ""
# for x in range(minX,maxX):
#     line += str(x) + " "
# print(line)
# line = ""
# for y in range(minY,maxY):
#     line += str(y) + " "
# print(line)

# for key in cave.keys():
#     print(key,cave[key])

# print(originals)

def print_cave():
    for i in range(minY,maxY):
        line = ""
        for j in range(minX,maxX):
            if not (j,i) in cave.keys():
                    cave[(j,i)] = "."

            line += cave[(j,i)]
        print(line)

print_cave()
sandsrc = (500,0)
lastRest = (0,0)
rested = []
sand = sandsrc
while lastRest != sandsrc:
    # if len(rested) % 100 == 0:
    #     print_cave()
    if sand == lastRest:
        sand = sandsrc
    if cave[(sand[0],sand[1]+1)] == ".":
        newSand = (sand[0],sand[1]+1)
    elif cave[(sand[0]-1,sand[1]+1)] == ".":
        newSand = (sand[0]-1,sand[1]+1)
    elif cave[(sand[0]+1,sand[1]+1)] == ".":
        newSand = (sand[0]+1,sand[1]+1)
    else:
        rested.append(sand)
        lastRest = sand
        newSand = sand
    cave[sand] = "."
    cave[newSand] = "o"
    sand = newSand
    # if sand[1] == maxY-1:
    #     break

print(rested)
print_cave()
print(len(rested))