#!/usr/bin/env python

inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

class ElfComms():
    def __init__(self, commandlist):
        self.cmdList = commandlist
        # print(self.cmdList, len(self.cmdList))
        self.cmd = 0
        self.X = 1
        self.clock = 0
        self.add = 0
        self.cmdState = 1
        self.value = 0
        self.CRT = {}
        for i in range(6):
            self.CRT[i] = []
            # for j in range(40):
            #     self.CRT[i].append('.')
        self.Xpositions = []

        
        self.magicCycles = {}
        for i in range(20, 240, 40):
            self.magicCycles[i] = 0
        self.magicIndex = 20

    def __str__(self):
        screen = ""
        # screen += str(self.clock) + " " + str(self.X) + " " + str(self.cmd) + "\n"
        # screen += "0123456789"*4 + "\n"
        for i in range(6):
            for j in range(40):
                screen += self.CRT[i][j]
            screen += "\n"
        return screen

    def drawPixel(self):
        position = self.clock - 1
        theline = 0
        while position > 39:
            position -= 40
            theline += 1

        if position == self.X - 1 \
            or position == self.X \
            or position == self.X + 1:
            self.CRT[theline].append("#")

        else:
            self.CRT[theline].append(".")


    def cycle(self):
        self.clock += 1
        self.drawPixel()

        if self.cmdState == 0:
            self.add = 1
        elif self.cmdState == 1:
            command = self.cmdList[self.cmd].split(" ")

            # print(self.clock, command)
            if command[0] == "addx":
                self.cmdState = 0
                self.value = int(command[1])
                self.cmd += 1

            elif command[0] == "noop":
                self.cmdState = 1
                self.cmd += 1

        if self.clock == self.magicIndex:
            self.magicCycles[self.clock] = self.clock * self.X
            self.magicIndex += 40

        if self.add == 1:
            self.X += self.value
            self.add = 0
            self.value = 0
            self.cmdState = 1

        self.Xpositions.append(self.X)

    def printP1(self):
        print(sum(self.magicCycles.values()))




elfcomms = ElfComms(data_list)

while elfcomms.clock < 240:
    elfcomms.cycle()


print(elfcomms)
elfcomms.printP1()
print(elfcomms.magicCycles)

print(max(elfcomms.Xpositions))