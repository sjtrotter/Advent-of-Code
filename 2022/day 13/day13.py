#!/usr/bin/env python
import json

inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

packets = {}
index = 1
packet = "left"
for line in data_list:
    if line != "":
        if not index in packets:
            packets[index] = {}
        packets[index][packet] = json.loads(line)
        if packet == "left":
            packet = "right"
        else:
            packet = "left"
            index += 1


def int_to_list(value):
    if isinstance(value, int):
        return [value]
 
def compare(v1, v2):
    print("comparing",v1,",",v2)
    if isinstance(v1, int) and isinstance(v2, int):
        if v1 < v2:
            print(v1,"<",v2)
            return True
        if v1 > v2:
            print(v1,">",v2)
            return False
        if v1 == v2:
            print(v1,"==",v2)
            return "="
    if isinstance(v1, list) and isinstance(v2, int):
        v2 = int_to_list(v2)
        return compare(v1,v2)
    if isinstance(v1, int) and isinstance(v2, list):
        v1 = int_to_list(v1)
        return compare(v1,v2)
    if isinstance(v1, list) and isinstance(v2,list):
        l1 = len(v1)
        l2 = len(v2)
        if v1 and not v2:
            return False
        if l1 <= l2:
            for i in range(l1):
                result = compare(v1[i],v2[i])
                if result == "=":
                    pass
                elif result:
                    pass
                else:
                    return result
        else:
            for i in range(l2):
                result = compare(v1[i],v2[i])
                if result == "=":
                    pass
                elif result:
                    pass
                else:
                    return result

    return True
    

print(packets)


ordered = []
for key in packets.keys():
    order = False
    print(packets[key])
    l1 = len(packets[key]["left"])
    l2 = len(packets[key]["right"])
    if l1 <= l2:
        order = compare(packets[key]["left"], packets[key]["right"])
    # else:
    #     order = False

    print(order)
    if order:
        ordered.append(int(key))

print(ordered)
print(sum(ordered))
