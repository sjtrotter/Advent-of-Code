#!/usr/bin/env python

inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

X = 1
cycle = 0
cmdReady = 1
adding = 0
cmd = 0
magicCycles = {}
for i in range(20, 240, 40):
    magicCycles[i] = 0
magicIndex = 20

while cycle < 220:
    cycle += 1
    if cmdReady == 0:
        adding = 1
    if cmdReady == 1:
        command = data_list[cmd].split(" ")
        # print(cycle, command)
        if command[0] == "addx":
            cmdReady = 0
            value = int(command[1])
        elif command[0] == "noop":
            cmdReady = 1
        else:
            print("error: bad input")
            exit()
        cmd += 1
    else:
        pass
        # print(cycle)

    if cycle == magicIndex:
        magicCycles[cycle] = cycle * X
        magicIndex += 40

    if adding == 1:
        X += value
        adding = 0
        cmdReady = 1


print(magicCycles)
print(sum(magicCycles.values()))