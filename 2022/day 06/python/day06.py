#!/usr/bin/env python

inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

markers = []
for line in data_list:
    linelist = list(line)
    # print(linelist)
    index = 13
    for i in range(13,len(linelist)):
        comp = linelist[index-13:index+1]
        print(comp)
        matching = False
        for j in range(0,len(comp)):
            if comp.count(comp[j]) > 1:
                matching = True
                break
        if matching == False:
            print(comp)
            markers.append(index + 1)
            break
        index += 1

print(markers)