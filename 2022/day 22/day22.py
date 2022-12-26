#!/usr/bin/env python

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
    map = {}
    directions = ""

    f = open(inputfile, "r")
    data = f.readlines()
    f.close()

    data_list = []
    for line in data:
        data_list.append(line.strip('\n'))

    directions = data_list.pop()
    data_list.pop()
    
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            if data_list[i][j] != " ":
                map[(j+1,i+1)] = data_list[i][j]

    return (map,directions)


# do stuff for the problem here - classes, functions, etc

class Move():
    def __init__(self, map, directions):
        self.map = map
        self.directions = directions
        self.calcs(self.map)
        self.maxX += 1
        self.maxY += 1
        self.currentPosition = self.getStartPosition()
        debug(str(self.currentPosition))
        self.facingValue = {
            "R": 0,
            "D": 1,
            "L": 2,
            "U": 3
        }
        
        self.currentFacing = "U"
        self.dirs = []
        self.dirs.append("R")
        num = ""
        for char in self.directions:
            if not char.isnumeric():
                nextDir = char
                self.dirs.append(int(num))
                self.dirs.append(nextDir)
                num = ""
            else:
                num += char
        self.dirs.append(int(num))
        debug(self.dirs)
        for direction in self.dirs:
            if not str(direction).isnumeric():
                self.currentFacing = self.faceDirection(direction)
            else:
                self.moveAhead(direction)
        

    def faceDirection(self, direction):
        if direction == "R":
            if self.currentFacing == "R":
                return "D"
            if self.currentFacing == "D":
                return "L"
            if self.currentFacing == "L":
                return "U"
            if self.currentFacing == "U":
                return "R"
        elif direction == "L":
            if self.currentFacing == "R":
                return "U"
            if self.currentFacing == "U":
                return "L"
            if self.currentFacing == "L":
                return "D"
            if self.currentFacing == "D":
                return "R"

    def moveAhead(self,steps):
        for x in range(1,steps+1):
            if not self.moveStep():
                return

    def moveStep(self):
        debug("moving from:"+str(self.currentPosition))
        x,y = self.currentPosition
        if self.currentFacing == "R":
            if (x+1,y) in self.map.keys():
                if self.map[(x+1,y)] == "#":
                    return False
                elif self.map[(x+1,y)] == ".":
                    self.currentPosition = (x+1,y)
                    return True
            else:
                for i in range(self.minX,x):
                    if (i,y) in self.map.keys():
                        if self.map[(i,y)] == "#":
                            return False
                        elif self.map[(i,y)] == ".":
                            self.currentPosition = (i,y)
                            return True

        if self.currentFacing == "L":
            if (x-1,y) in self.map.keys():
                if self.map[(x-1,y)] == "#":
                    return False
                elif self.map[(x-1,y)] == ".":
                    self.currentPosition = (x-1,y)
                    return True
            else:
                for i in range(self.maxX,x,-1):
                    if (i,y) in self.map.keys():
                        if self.map[(i,y)] == "#":
                            return False
                        elif self.map[(i,y)] == ".":
                            self.currentPosition = (i,y)
                            return True

        if self.currentFacing == "D":
            if (x,y+1) in self.map.keys():
                if self.map[(x,y+1)] == "#":
                    return False
                elif self.map[(x,y+1)] == ".":
                    self.currentPosition = (x,y+1)
                    return True
            else:
                for i in range(self.minY,y):
                    if (x,i) in self.map.keys():
                        if self.map[(x,i)] == "#":
                            return False
                        elif self.map[(x,i)] == ".":
                            self.currentPosition = (x,i)
                            return True

        if self.currentFacing == "U":
            if (x,y-1) in self.map.keys():
                if self.map[(x,y-1)] == "#":
                    return False
                elif self.map[(x,y-1)] == ".":
                    self.currentPosition = (x,y-1)
                    return True
            else:
                for i in range(self.maxY,y,-1):
                    if (x,i) in self.map.keys():
                        if self.map[(x,i)] == "#":
                            return False
                        elif self.map[(x,i)] == ".":
                            self.currentPosition = (x,i)
                            return True


    def getStartPosition(self):
        y = self.minY
        for x in range(self.minX,self.maxX):
            if (x,y) in self.map.keys():
                if self.map[(x,y)] == ".":
                    break
        return (x,y)





    def __str__(self):
        string = ""
        for y in range(1,self.maxY):
            length = 0
            for x in range(1,self.maxX):
                if (x,y) in self.map.keys():
                    debug(str(x)+","+str(y))
                    string += self.map[(x,y)]
                else:
                    string += " "
                # length += 1
            string += "\n"
        
        # print(string)
        return string


    def calcs(self, map):
        self.minX = 5
        self.maxX = 5
        self.minY = 5
        self.maxY = 5

        for key in self.map.keys():
            if key[0] < self.minX: self.minX = key[0]
            if key[1] < self.minY: self.minY = key[1]
            if key[0] > self.maxX: self.maxX = key[0]
            if key[1] > self.maxY: self.maxY = key[1]

    def getPassword(self):
        debug(str(self.currentPosition))
        debug(str(self.currentFacing))
        return (self.currentPosition[1] * 1000) + \
                (self.currentPosition[0] * 4) + \
                self.facingValue[self.currentFacing]
            




if __name__ == "__main__":
    debug("determining input file...")
    inputfile = determine_input(sys.argv)
    if not inputfile:
        print("no suitable input found:",inputfile)
        exit(1)
    
    debug(["parsing input file: ",inputfile])
    map,directions = parse_input(inputfile)
    debug(str(map))
    debug(directions)
    move = Move(map,directions)
    debug("\n"+str(move))
    print(move.getPassword())
    # call functions, print output for solutions