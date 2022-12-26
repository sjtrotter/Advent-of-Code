#!/usr/bin/python

inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())


doubleduties = 0
overlappies = 0
for line in data_list:
    half1, half2 = line.split(',')
    start1, stop1 = half1.split('-')
    start2, stop2 = half2.split('-')
    start1 = int(start1)
    start2 = int(start2)
    # stop1 = int(stop1) +1
    # stop2 = int(stop2) +1
    stop1 = int(stop1)
    stop2 = int(stop2)
    # elf1 = ''
    # elf2 = ''

    if (start1 <= start2 and stop1 >= stop2) or  (start2 <= start1 and stop2 >= stop1):
            # print("elf2 (", half2, ") is inside elf1:", half1)
            doubleduties += 1
    #         continue
    # elif start2 <= start1 and stop2 >= stop1:
    #         print("elf1 (", half1, ") is inside elf2:", half2)
    #         doubleduties += 1
    #         continue

    if start1 in range(start2, stop2+1) or stop1 in range(start2, stop2+1):
        overlappies += 1
        continue

    if start2 in range(start1, stop1+1) or stop2 in range(start1, stop1+1):
        overlappies += 1

    # for i in range(start1, stop1):
    #     elf1 += str(i)
    # for i in range(start2, stop2):
    #     elf2 += str(i)
    # print(elf1)
#     print("line:", line)
#     print("half1:", half1)
#     print("half2:", half2)
#     print("start1", start1)
#     print("start2", start2)
#     print("stop1", stop1)
#     print("stop2", stop2)
#     range1 = ''.join(range(start1, stop1))
#     range2 = ''.join(range(start2, stop2))
    # if elf1 in elf2 or elf2 in elf1:
    #     doubleduties += 1
    #     print("elf1:", half1, start1, stop1, elf1)
    #     print("elf2:", half2, start2, stop2, elf2)

print(doubleduties)
print(overlappies)