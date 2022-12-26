#!/usr/bin/env python

class Elf():

    def __init__(self,x,y,grid):

        self.position = (x,y)
        self.grid = grid
        
        self.grid.plot(x,y)
        self.proposal = self.position

    
    def __str__(self):

        return "("+str(self.position[0])+","+str(self.position[1])+") "


    def move(self,x,y):
        
        self.grid.clear(self.position[0],self.position[1])
        self.grid.plot(x,y)
        self.position = (x,y)


    def propose(self,directions):
        x = self.position[0]
        y = self.position[1]
        # check all sides first, if clear
        # return (None,None)
        if self.grid.check(x-1,y-1) and \
            self.grid.check(x-1,y) and \
            self.grid.check(x-1,y+1) and \
            self.grid.check(x,y-1) and \
            self.grid.check(x,y+1) and \
            self.grid.check(x+1,y-1) and \
            self.grid.check(x+1,y) and \
            self.grid.check(x+1,y+1):
            self.proposal = self.position
            return self.proposal
        # otherwise, for dir in directions
        # - check direction prereqs
        # - if clear, propose (return) coords
        # - if not, pass to next
        # at end, return (None,None)
        for direction in directions:
            if direction == "N":
                if self.grid.check(x-1,y-1) and \
                    self.grid.check(x,y-1) and \
                    self.grid.check(x+1,y-1):
                    self.proposal = (x,y-1)
                    return self.proposal

            if direction == "S":
                if self.grid.check(x-1,y+1) and \
                    self.grid.check(x,y+1) and \
                    self.grid.check(x+1,y+1):
                    self.proposal = (x,y+1)
                    return self.proposal
            if direction == "W":
                if self.grid.check(x-1,y+1) and \
                    self.grid.check(x-1,y) and \
                    self.grid.check(x-1,y-1):
                    self.proposal = (x-1,y)
                    return self.proposal
            if direction == "E":
                if self.grid.check(x+1,y+1) and \
                    self.grid.check(x+1,y) and \
                    self.grid.check(x+1,y-1):
                    self.proposal = (x+1,y)
                    return self.proposal

        self.proposal = self.position
        return self.proposal