#!/usr/bin/env python
import json
from functools import cmp_to_key


inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

def parse(data):
    packets = {}
    index = 1
    packet = "left"
    for line in data:
        if line != "":
            if not index in packets:
                packets[index] = {}
            packets[index][packet] = json.loads(line)
            if packet == "left":
                packet = "right"
            else:
                packet = "left"
                index += 1
    return packets

packets = parse(data_list)

def int_to_list(value):
    if isinstance(value, int):
        return [value]
 
def compare(v1, v2):
    # print("comparing",v1,",",v2)
    if isinstance(v1, int) and isinstance(v2, int):
        if v1 < v2:
            # print(v1,"<",v2)
            return True
        if v1 > v2:
            # print(v1,">",v2)
            return False

    if isinstance(v1, list) and isinstance(v2, int):
        v2 = int_to_list(v2)
        return compare(v1,v2)
    if isinstance(v1, int) and isinstance(v2, list):
        v1 = int_to_list(v1)
        return compare(v1,v2)

    if isinstance(v1, list) and isinstance(v2,list):
        maxLen = max(len(v1),len(v2))
        for i in range(maxLen):
            if i == len(v1) and i < len(v2):
                return True
            if i < len(v1) and i == len(v2):
                return False
            result = compare(v1[i],v2[i])
            if result is not None:
                return result
            
    return None

# print(packets)


ordered = []
for key in packets.keys():
    order = None
    # print(packets[key])
    
    order = compare(packets[key]["left"],packets[key]["right"])
    
    # print(order)
    if order == True:
        ordered.append(int(key))

# print(ordered)
print("part1:", sum(ordered))

orderedPackets = {}
data_list.append("")
data_list.append("[[2]]")
data_list.append("[[6]]")
packettmp = parse(data_list)
packets = []
for key in packettmp.keys():
    packets.append(packettmp[key]["left"])
    packets.append(packettmp[key]["right"])

for i in range(0,len(packets)):
    for j in range(0,len(packets)-i-1):
        if not compare(packets[j],packets[j+1]):
            tmp = packets[j]
            packets[j] = packets[j+1]
            packets[j+1] = tmp


# print(packets)

index2 = packets.index([[2]])+1
index6 = packets.index([[6]])+1

print("part2",index2*index6)