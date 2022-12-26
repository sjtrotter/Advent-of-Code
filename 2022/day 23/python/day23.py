#!/usr/bin/env python
import grid
import os,sys
global DEBUG
global YELLOW

DEBUG = ("-v" in sys.argv)
YELLOW = "\033[1;33m"
CLEAR = "\033[0;0m"

def debug(msg):
    if DEBUG:
        string = YELLOW + "[+] " + CLEAR
        for item in msg:
            string += str(item)
        print(string)

def determine_input(argv):
    if len(argv) > 1:
        if os.path.exists(argv[-1]):
            return argv[-1]
        elif "-t" in argv:
            if os.path.exists("test.txt"):
                return "test.txt"
        else:
            if os.path.exists("input.txt"):
                return "input.txt"
    return None

def parse_input(inputfile):
    # define parsing here
    f = open(inputfile, "r")
    data = f.readlines()
    f.close()

    data_list = []
    for line in data:
        data_list.append(line.strip('\n'))

    data_dict = {}
    for y in range(len(data_list)):
        for x in range(len(data_list[y])):
            if data_list[y][x] == "#":
                data_dict[(x,y)] = "#"

    return data_dict



# do stuff for the problem here - classes, functions, etc

class Elf():
    def __init__(self,x,y):

        self.x = x
        self.y = y
        self.consider = ["N","S","W","E"]
        self.decision = ""

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+") "

    def checkN(self):
        if (self.x,self.y-1) in data.keys() and data[(self.x,self.y-1)] == "#":
            return False
        else:
            return True

    def checkNW(self):
        if (self.x-1,self.y-1) in data.keys() and data[(self.x-1,self.y-1)] == "#":
            return False
        else:
            return True

    def checkW(self):
        if (self.x-1,self.y) in data.keys() and data[(self.x-1,self.y)] == "#":
            return False
        else:
            return True

    def checkSW(self):
        if (self.x-1,self.y+1) in data.keys() and data[(self.x-1,self.y+1)] == "#":
            return False
        else:
            return True

    def checkS(self):
        if (self.x,self.y+1) in data.keys() and data[(self.x,self.y+1)] == "#":
            return False
        else:
            return True

    def checkSE(self):
        if (self.x+1,self.y+1) in data.keys() and data[(self.x+1,self.y+1)] == "#":
            return False
        else:
            return True

    def checkE(self):
        if (self.x+1,self.y) in data.keys() and data[(self.x+1,self.y)] == "#":
            return False
        else:
            return True

    def checkNE(self):
        if (self.x+1,self.y-1) in data.keys() and data[(self.x+1,self.y-1)] == "#":
            return False
        else:
            return True

    def lookAround(self):
        if self.checkN() and self.checkNW() and self.checkW() \
            and self.checkSW() and self.checkS() and self.checkSE() and \
            self.checkE() and self.checkNE():
            return None
        for direction in self.consider:
            if direction == "N" and self.checkN() and \
                self.checkNE() and self.checkNW():
                debug("chose N")
                return "N"
            if direction == "S" and self.checkS() and \
                self.checkSE() and self.checkSW():
                debug("chose S")
                return "S"
            if direction == "W" and self.checkW() and \
                self.checkNW() and self.checkSW():
                debug("chose W")
                return "W"
            if direction == "E" and self.checkE() and \
                self.checkNE() and self.checkSE():
                debug("chose E")
                return "E"


    def decideMove(self):
        decision = self.lookAround()
        if decision == None:
            self.decision = (self.x,self.y)
            return self.decision
        self.consider.append(self.consider.pop(0))
        x = 0
        y = 0
        if decision == "N":
            x = self.x
            y = self.y - 1
        if decision == "S":
            x = self.x
            y = self.y + 1
        if decision == "W":
            x = self.x - 1
            y = self.y
        if decision == "E":
            x = self.x + 1
            y = self.y

        self.decision = (x,y)
        return self.decision

    def makeMove(self):
        data[(self.x,self.y)] = "."
        self.x, self.y = self.decision
        data[(self.x,self.y)] = "#"



if __name__ == "__main__":
    
    debug("determining input file...")
    inputfile = determine_input(sys.argv)
    if not inputfile:
        print("no suitable input found:",inputfile)
        exit(1)
    
    debug(["parsing input file: ",inputfile])
    data = parse_input(inputfile)

    elves = []

    for coord in data.keys():
        elves.append(Elf(coord[0],coord[1]))

    debug(elves)

    # minX = 0
    # maxX = 0
    # minY = 0
    # maxY = 0
    # for key in data.keys():
    #     if key[0] > maxX: maxX = key[0]
    #     if key[0] < minX: minX = key[0]
    #     if key[1] > maxY: maxY = key[1]
    #     if key[1] < minY: minY = key[0]

    # maxX += 1
    # maxY += 1
    # string = ""
    # for y in range(minY,maxY):
    #     line = ""
    #     for x in range(minX,maxX):
    #         if (x,y) not in data.keys():
    #             data[(x,y)] = '.'
    #         string += data[(x,y)]
    #     string += "\n"

    # print(string)

    cycle = 0
    while cycle < 10:
        cycle += 1
        goodDecisions = set()
        badDecisions = set()
        for elf in elves:
            move = (elf,elf.decideMove())
            for decision in goodDecisions:
                if decision[1] == move[1]:
                    badDecisions.add(move)
            if move not in badDecisions:
                goodDecisions.add(move)
        for move in badDecisions:
            temp = set(goodDecisions)
            for decision in temp:
                if decision[1] == move[1]:
                    goodDecisions.remove(decision)
        for move in goodDecisions:
            move[0].makeMove()
        
    debug([data.keys(),data.values()])
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    for key in data.keys():
        if key[0] > maxX: maxX = key[0]
        if key[0] < minX: minX = key[0]
        if key[1] > maxY: maxY = key[1]
        if key[1] < minY: minY = key[0]

    maxX += 1
    maxY += 1
    string = ""
    for y in range(minY,maxY):
        line = ""
        for x in range(minX,maxX):
            if (x,y) not in data.keys():
                data[(x,y)] = '.'
            string += data[(x,y)]
        string += "\n"

    print(string)
    
    count = 0
    for v in data.values():
        if v == '.':
            count += 1

    print(count)


    # call functions, print output for solutions