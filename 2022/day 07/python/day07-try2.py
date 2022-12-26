#!/usr/bin/env python

inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

dir = []
dirs = {}
files = {}
for line in data_list:
    exploded = line.split(" ")
    if exploded[0] == "$":
        if exploded[1] == "cd":
            if exploded[2] == "..":
                dir.pop()
            else:
                dir.append(exploded[2])
                if not "/".join(dir) in dirs.keys():
                    dirs["/".join(dir)] = []

    elif exploded[0].isnumeric():
        files[exploded[1]] = int(exploded[0])
        dirs["/".join(dir)].append(exploded[1])

    elif exploded[0] == "dir":
        if not "/".join(dir) +"/"+exploded[1] in dirs.keys():
            dirs["/".join(dir) +"/"+exploded[1]] = []
        dirs["/".join(dir)].append("/".join(dir)+"/"+exploded[1])

# for dir in dirs.keys():
#     print(dir, dirs[dir])

# for file in files.keys():
#     print(file)

def calculate(dir): # recursion depth is too large for full dataset
    size = 0
    for file in dir:
        if file in dirs.keys():
            if not bool(dirs[file]):
                continue
            else:
                size += calculate(dirs[file])
        else:
            size += files[file]
    return size

dirsizes = {}

dirlist = ['/']

for dir in dirs.keys():
    if not dir in dirlist:
        for i in range(len(dirlist)):
            if len(dir) > len(dirlist[i]):
                dirlistTMP = dirlist[i:]
                dirlist = [dir]
                for eachdir in dirlistTMP:
                    dirlist.append(eachdir)
                break
            else:
                dirlist.append(eachdir)
                break

for e in dirlist:
    print(e)

print(len(dirlist),len(dirs.keys()))


index = 0
for dir in dirs.keys():
    dirsizes[dirlist[index]] = calculate(dirs[dirlist[index]])
    index += 1

total = 0
for dir in dirsizes.keys():
    print(dir, dirsizes[dir])
    if dirsizes[dir] < 100000:
        total += dirsizes[dir]

print (total)