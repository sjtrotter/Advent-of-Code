#!/usr/bin/env python

inputfile = open("input.txt", "r")

data = inputfile.readlines()

inputfile.close()

data_list = []

for line in data:
    data_list.append(line.strip())

# print(data_list[0:20])

data_dict = {}
i=0
elf=1

for line in data_list:
    if (line == ''):
        data_dict['elf' + str(elf)] = i
        i = 0
        elf += 1
        continue
    i += int(line)

# print(data_dict)

top_three = []

for x in range(1,4):
    key = max(data_dict, key=data_dict.get)
    # print(data_dict[key])
    top_three.append(data_dict[key])
    del(data_dict[key])

print("top three:", top_three)
print("sum:",sum(top_three))
