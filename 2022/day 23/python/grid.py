#!/usr/bin/env python

class Grid():

    def __init__(self,width,height,debug=False,blank="."):

        self.width = width
        self.height = height
        self.minX = 0
        self.minY = 0
        self.maxX = self.width
        self.maxY = self.height
        self.blank = blank
        self.debug = debug

        self.grid = {}
        for y in range(self.minY,self.maxY):
            for x in range(self.minX,self.maxX):
                self.grid[(x,y)] = self.blank


    def __str__(self):

        string = "\n"
        for y in range(self.minY,self.maxY):
            for x in range(self.minX,self.maxX):
                string += self.grid[(x,y)]
            string += "\n"

        return string


    def debug_print(self,msg):
        # Use ANSI escape codes to set the text color to yellow
        if self.debug:
            print('\033[33m[+]\033[0m', msg)


    def grow(self,axis,size=1):

        if axis == "x":
            if abs(size) == size:
                self.maxX += size
                self.debug_print("new maxX: "+str(self.maxX))
            else:
                self.minX += size
                self.debug_print("new minX: "+str(self.minX))
        elif axis == "y":
            if abs(size) == size:
                self.maxY += size
                self.debug_print("new maxY: "+str(self.maxY))
            else:
                self.minY += size
                self.debug_print("new minY: "+str(self.minY))

        self.debug_print("adding new row/column...")
        for y in range(self.minY,self.maxY):
            for x in range(self.minX,self.maxX):
                if (x,y) not in self.grid.keys():
                    self.grid[(x,y)] = self.blank


    def check(self,x,y):
        # check if out of grid, so we can grow
        if (x,y) not in self.grid.keys():
            if x < self.minX:
                self.debug_print("shrinking grid minX")
                self.grow("x",-1)
            if x > self.maxX-1:
                self.debug_print("adding grid maxX")
                self.grow("x",1)
            if y < self.minY:
                self.debug_print("shrinking grid minY")
                self.grow("y",-1)
            if y > self.maxY-1:
                self.debug_print("adding grid maxY")
                self.grow("y",1)
                
        if self.grid[(x,y)] == self.blank:
            return True
        else:
            return False

    def plot(self,x,y,char="#"):

        if len(char) > 1:
            raise ValueError(char+" is too large.")

        if (x,y) in self.grid.keys():
            self.grid[(x,y)] = char
            return True
        else:
            raise KeyError("("+str(x)+","+str(y)+") is not in Grid.")

    def clear(self,x,y):
        
        self.plot(x,y,self.blank)


    def countBlanks(self):

        minX = 0
        maxX = 0
        minY = 0
        maxY = 0

        for key in self.grid.keys():
            if self.grid[key] != self.blank:
                if key[0] > maxX: maxX = key[0]
                if key[0] < minX: minX = key[0]
                if key[1] > maxY: maxY = key[1]
                if key[1] < minY: minY = key[1]

        count = 0
        for y in range(minY,maxY+1):
            for x in range(minX,maxX+1):
                if self.grid[(x,y)] == self.blank:
                    count += 1
        
        return count