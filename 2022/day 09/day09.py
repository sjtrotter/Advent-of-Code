#!/usr/bin/env python

inputfile = open("input2.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

class Rope():
    def __init__(self, width, height):
        startx = int(width / 2)
        starty = int(height / 2)
        self.knots = []
        for i in range(10):
            self.knots.append([startx,starty])
        self.width = width
        self.height = height
        self.tailmoves = ["["+str(startx)+","+str(starty)+"]"]
        self.grid = {}
        for x in range(width):
            for y in range(height):
                self.grid["["+str(x)+","+str(y)+"]"] = "."
        self.grid[self.tailmoves[0]] = "#"



    def __str__(self):
        string = "head: " + str(self.knots[0]) + " tail: " + str(self.knots[9]) + "\n" \
            + str(self.tailmoves) +"\n"
        for y in range(self.height-1,-1,-1):
            line = ""
            for x in range(self.width):
                line += self.grid["["+str(x)+","+str(y)+"]"]
            string += line + "\n"


        return string

    def getHead(self):
        return self.knots[0]

    def move(self, direction, steps):
        # move the head
        orighead = self.knots[0]
        origtail = self.knots[9]

        if direction == "L":
            mv = [-1,0]
        elif direction == "R":
            mv = [1,0]
        elif direction == "U":
            mv = [0,1]
        elif direction == "D":
            mv = [0,-1]

        for step in range(1, steps+1):
            # headlast = [self.knots[0][0], self.knots[0][1]]
            # onelast = [self.knots[1][0], self.knots[1][1]]
            # twolast = [self.knots[2][0], self.knots[2][1]]
            # threelast = [self.knots[3][0], self.knots[3][1]]
            # fourlast = [self.knots[4][0], self.knots[4][1]]
            # fivelast = [self.knots[5][0], self.knots[5][1]]
            # sixlast = [self.knots[6][0], self.knots[6][1]]
            # sevenlast = [self.knots[7][0], self.knots[7][1]]
            # eightlast = [self.knots[8][0], self.knots[8][1]]
            print(self.knots[0],self.knots[1],self.knots[2],self.knots[3],self.knots[4],self.knots[5],self.knots[6],self.knots[7],self.knots[8],self.knots[9])
            self.knots[0][0] = self.knots[0][0] + mv[0]
            self.knots[0][1] = self.knots[0][1] + mv[1]
            # tailmoved = 0

            for i in range(1,10):
                if abs(self.knots[i-1][0] - self.knots[i][0]) == 2 \
                    and self.knots[i-1][1] - self.knots[i][1] == 0:
                    if i == 9 and \
                        not "["+str(self.knots[9][0])+","+str(self.knots[9][1])+"]" in self.tailmoves:
                        self.tailmoves.append("["+str(self.knots[9][0])+","+str(self.knots[9][1])+"]")
                        self.grid["["+str(self.knots[9][0])+","+str(self.knots[9][1])+"]"] = "#"

                    if self.knots[i-1][0]-self.knots[i][0] > 0:
                        self.knots[i][0] += 1
                    else:
                        self.knots[i][0] -= 1

                elif abs(self.knots[i-1][1] - self.knots[i][1]) == 2 \
                    and self.knots[i-1][0] - self.knots[i][0] == 0:
                    if i == 9 and \
                        not "["+str(self.knots[9][0])+","+str(self.knots[9][1])+"]" in self.tailmoves:
                        self.tailmoves.append("["+str(self.knots[9][0])+","+str(self.knots[9][1])+"]")
                        self.grid["["+str(self.knots[9][0])+","+str(self.knots[9][1])+"]"] = "#"

                    if self.knots[i-1][0]-self.knots[i][0] > 0:
                        self.knots[i][0] += 1
                    else:
                        self.knots[i][0] -= 1

                elif abs(self.knots[i-1][0] - self.knots[i][0]) == 2 \
                    and abs(self.knots[i-1][1] - self.knots[i][1]) == 1:
                    if i == 9 and \
                        not "["+str(self.knots[9][0])+","+str(self.knots[9][1])+"]" in self.tailmoves:
                        self.tailmoves.append("["+str(self.knots[9][0])+","+str(self.knots[9][1])+"]")
                        self.grid["["+str(self.knots[9][0])+","+str(self.knots[9][1])+"]"] = "#"

                    self.knots[i][1] += (self.knots[i-1][1] - self.knots[i][1])

                    if self.knots[i-1][0]-self.knots[i][0] > 0:
                        self.knots[i][0] += 1
                    else:
                        self.knots[i][0] -= 1

                elif abs(self.knots[i-1][1] - self.knots[i][1]) == 2 \
                    and abs(self.knots[i-1][0] - self.knots[i][0]) == 1:
                    if i == 9 and \
                        not "["+str(self.knots[9][0])+","+str(self.knots[9][1])+"]" in self.tailmoves:
                        self.tailmoves.append("["+str(self.knots[9][0])+","+str(self.knots[9][1])+"]")
                        self.grid["["+str(self.knots[9][0])+","+str(self.knots[9][1])+"]"] = "#"

                    self.knots[i][0] += (self.knots[i-1][0] - self.knots[i][0])

                    if self.knots[i-1][1]-self.knots[i][1] > 0:
                        self.knots[i][1] += 1
                    else:
                        self.knots[i][1] -= 1


            # if abs(self.knots[8][0] - self.knots[9][0]) > 1 \
            #     or abs(self.knots[8][1] - self.knots[9][1]) > 1:
            #     self.knots[9][0] = eightlast[0]
            #     self.knots[9][1] = eightlast[1]


                # if not "["+str(self.knots[9][0])+","+str(self.knots[9][1])+"]" in self.tailmoves:
                #     self.tailmoves.append("["+str(self.knots[9][0])+","+str(self.knots[9][1])+"]")
                #     self.grid["["+str(self.knots[9][0])+","+str(self.knots[9][1])+"]"] = "#"
                    
            # elif abs(self.knots[0][1] - self.tail[1]) > 1 \
            #     and not abs(self.knots[0][0] - self.tail[0]) > 1:
            #     tailmoved = 1
            #     self.tail = headlast
                # self.tail[1] = self.tail[1] + mv[1]
            # self.tailmoves += tailmoved
gridLength = 0
gridHeight = 0

for line in data_list:
    direction, steps = line.split(" ")
    if direction == "L" or direction == "R":
        gridLength += int(steps)
    elif direction == "U" or direction == "D":
        gridHeight += int(steps)



rope = Rope(gridLength, gridHeight)
print(rope)
for line in data_list:
    direction, steps = line.split(" ")
    rope.move(direction, int(steps))

print(rope)
print (len(rope.tailmoves))