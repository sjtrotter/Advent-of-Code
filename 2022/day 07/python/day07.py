#!/usr/bin/env python

inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

dirs = {}
files = {}
curdir = []
for line in data_list:

    exploded = line.split(' ')
    if exploded[0] == "$":
        if exploded[1] == "cd":

            if exploded[2] == "..":
                # dirsizes[lastdir] += dirsizes[curdir]
                curdir.pop()
            else:
                curdir.append(exploded[2])

            if not '/'.join(curdir) in dirs.keys():
                dirs['/'.join(curdir)] = []
    
    else:
        # print(line)
        # print(exploded)
        if exploded[0] == "dir":
            dirs['/'.join(curdir)].append('/'.join(curdir) + '/' + exploded[1])
        else:
            dirs['/'.join(curdir)].append(exploded[1])
        if exploded[0].isnumeric():
            files[exploded[1]] = int(exploded[0])
            


# print(dirs)
# print(files)
count = 0
for key in dirs.keys():
    count += 1
    print(count, key, dirs[key])


def calculate(dir, name):
    size = 0
    # print("calculating", name)
    done = True
    dirs = 0
    for file in dir:
        # print("... checking", file)
        if file in files.keys():
            # print("...", file, "in files, adding...")
            size += files[file]
        elif name+file in files.keys():
            size += files[name+file]
        else:
            # print("...", file, "not in files, keeping on going...")
            dirs += 1
            done = False
    if dirs == len(dir):
        done = True
    if done == True:
        # print("dir", name, "done, adding to files...")
        files[name] = size
    
    return size






# def calculate(dir): # recursion depth is too large for full dataset
#     size = 0
#     for file in dir:
#         if file in dirs.keys():
#             try:
#                 size += calculate(dirs[file])
#             except:
#                 pass
#         else:
#             size += files[file]
#     return size







sizes = {}
length = len(dirs.keys())
dirsdone = 0

while dirsdone < length:
        
    for dir in dirs.keys():
        if not dir in files.keys():
            print(dir, "still not in files")
            sizes[dir] = calculate(dirs[dir], dir)
        else:
            print("in files:",dir, files[dir])

    dirsdone = 0
    for dir in dirs.keys():
        # print("number of dirs:", length)
        if dir in files.keys():
            dirsdone += 1
        # print("dirs done:", dirsdone)
    
    # if dirsdone == 107:
    #     count = 0
    #     for key in dirs.keys():
    #         count += 1
    #         print(count, key)
    #     count = 0
    #     for key in files.keys():
    #         count += 1
    #         print(count, key)
    #     exit()


    print(dirsdone, "dirs done of", length)
    
print(sizes)

total = 0
for dir in sizes:
    if sizes[dir] <= 100000:
        total += sizes[dir]
        print(dir,sizes[dir])

print(total)


# for key in dirmap.keys():
#     print(key, dirmap[key])