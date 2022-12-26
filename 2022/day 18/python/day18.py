#!/usr/bin/env python

inputfile = open("input2.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

cubes = set()
for line in data_list:
    x,y,z = line.split(",")
    x = int(x)
    y = int(y)
    z = int(z)
    cubes.add((x,y,z))

totalSurface = 0
for cube in cubes:
    x,y,z = cube
    surface = 6
    if (x+1,y,z) in cubes:
        surface -= 1
    if (x-1,y,z) in cubes:
        surface -= 1
    if (x,y+1,z) in cubes:
        surface -= 1
    if (x,y-1,z) in cubes:
        surface -= 1
    if (x,y,z+1) in cubes:
        surface -= 1
    if (x,y,z-1) in cubes:
        surface -= 1
    totalSurface += surface

print(totalSurface)

contiguous = set()
maxX = 0
maxY = 0
maxZ = 0

for cube in cubes:
    x,y,z = cube
    if x > maxX:
        maxX = x
    if y > maxY:
        maxY = y
    if z > maxZ:
        maxZ = z

negative = set()
for x in range(maxX+1):
    for y in range(maxY+1):
        for z in range(maxZ+1):
            if not (x,y,z) in cubes:
                negative.add((x,y,z))
    

print(negative)
# print(cubes)

# remove outers from negative

removes = []

for cube in negative:
    x,y,z = cube
    exx = 0
    why = 0
    zee = 0
    for X in range(0,x):
        if (X,y,z) in cubes:
            exx = 1
    for X in range(x+1,maxX):
        if (X,y,z) in cubes:
            exx = 1
    for Y in range(0,y):
        if (x,Y,z) in cubes:
            why = 1
    for Y in range(y+1,maxY):
        if (x,Y,z) in cubes:
            why = 1
    for Z in range(0,z):
        if (x,y,Z) in cubes:
            zee = 1
    for Z in range(z+1,maxZ):
        if (x,y,Z) in cubes:
            zee = 1

    if sum([exx,why,zee]) > 0:
        removes.append((x,y,z))

for cube in removes:
    negative.discard(cube)

print(negative)

cubeSpaces = set()
for cube in negative:
    x,y,z = cube
    if  (x-1,y,z) in cubes \
    and (x+1,y,z) in cubes \
            and (x,y-1,z) in cubes \
            and (x,y+1,z) in cubes \
                and (x,y,z-1) in cubes \
                and (x,y,z+1) in cubes: # totally surrounded 1x1
                    cubeSpaces.add(cube)
    # else:
    #     if (x,y,z) not in cubeSpaces:
    #         for 




# totalSurface = 0
# for cube in cubes:
#     x,y,z = cube
#     surface = 6
#     for X in range(x):
#         if (X,y,z) in cubes:
#             surface -= 1
#     for X in range(x,maxX):
#         if (X,y,z) in cubes:
#             surface -= 1
#     for Y in range(y):
#         if (x,Y,z) in cubes:
#             surface -= 1
#     for Y in range(y,maxY):
#         if (x,Y,z) in cubes:
#             surface -= 1
#     for Z in range(z):
#         if (x,y,Z) in cubes:
#             surface -= 1
#     for Z in range(z,maxZ):
#         if (x,y,Z) in cubes:
#             surface -= 1
#     totalSurface += surface

# print(totalSurface)

print (totalSurface)