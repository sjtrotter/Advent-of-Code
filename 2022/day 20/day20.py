#!/usr/bin/env python

inputfile = open("input2.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
original = []
i = 0
N = ()
for line in data:
    j = int(line.strip())
    data_list.append((j,i))
    original.append((j,i))
    if j == 0:
        N = (j,i)

    i += 1


# print(data_list)

# new_list = []
# for i in range(len(data_list)):
#     new_list.append(0)

# for i in range(len(data_list)):
#     j = i + data_list[i]
#     if j > len(data_list):
#         j -= len(data_list)
#     if j < 0:
#         j += len(data_list)
#     new_list[j] = data_list[i]

# print(new_list)


# data_dict = {}
# original = data_list

# for i in range(len(data_list)):
#     data_dict[i] = i

index = 0
for item in original:
    # print(data_list)
    i = data_list.index(item)
    p = data_list.pop(i)
    d = p[0]
    # print(i,p)
    if i + d >= len(original):
        i = i + d - len(original) + 1
    elif i + d <= 0:
        i = i + d + len(original) - 1
    else:
        i += d
    data_list.insert(i,p)
    index += 1


print(data_list)

coords = []

j = data_list.index(N)
index = j
for i in range(0,1000):
    index += 1
    if index > len(data_list) - 1:
        index = 0
coords.append(data_list[index][0])


# j = data_list.index(0)
for i in range(0,1000):
    index += 1
    if index > len(data_list) - 1:
        index = 0
coords.append(data_list[index][0])


# j = data_list.index(0)
# index = 0
for i in range(0,1000):
    index += 1
    if index > len(data_list) - 1:
        index = 0
coords.append(data_list[index][0])



print(coords)
print(sum(coords))