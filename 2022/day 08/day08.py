#!/usr/bin/env python

inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

class VisibleForest():
    def __init__(self, grid):
        # grid is a list of strings

        self.forest = {}
        row = 0
        for line in grid:
            self.forest[row] = []
            for tree in line:
                self.forest[row].append(tree)
            row += 1

        self.length = len(self.forest[0])
        self.height = row

    def getHeight(self):
        return self.height
    
    def getLength(self):
        return self.length
        
    def __str__(self):
        string = ""
        for line in self.forest.keys():
            string += str(self.forest[line]) + "\n"

        return string

    def isVisible(self, tree):
        x = tree[0]
        y = tree[1]
        if x == 0 or x == self.length-1 or y == 0 or y == self.height-1:
            return True
        left = False
        right = False
        up = False
        down = False
        for i in range(self.length):
            if self.forest[y][i] >= self.forest[y][x]:
                if i < x: left = True
                if i > x: right = True
        for i in range(self.height):
            if self.forest[i][x] >= self.forest[y][x]:
                if i > y: down = True
                if i < y: up = True
        if left and right and up and down:
            return False
        else:
            return True
        
    def getScenicScore(self, tree):
        up = 0
        down = 0
        left = 0
        right = 0
        x = tree[0]
        y = tree[1]
        if x == 0: left = 0
        if y == 0: up = 0
        if x == self.length-1: right = 0
        if y == self.height-1: down = 0

        #left
        if x == 1: left = 1
        else:
            for i in range(x-1,-1,-1):
                left += 1
                if self.forest[y][i] >= self.forest[y][x]:
                    break
        
        #right
        if x == self.length-2: right = 1
        else:
            for i in range(x+1,self.length):
                right += 1
                if self.forest[y][i] >= self.forest[y][x]:
                    break
        
        #up
        if y == 1: up = 1
        else:
            for i in range(y-1,-1,-1):
                up += 1
                if self.forest[i][x] >= self.forest[y][x]:
                    break

        #down
        if y == self.height-2: down = 1
        else:
            for i in range(y+1,self.height):
                down += 1
                if self.forest[i][x] >= self.forest[y][x]:
                    break

        # print(x, y, left, right, up, down)
        result = left * right * up * down
        return result


                


forest = VisibleForest(data_list)

# print(forest)
# print(forest.isVisible((0,0)),forest.isVisible((0,1)),forest.isVisible((0,2)),forest.isVisible((0,3)),forest.isVisible((0,0)))
# print(forest.isVisible((1,0)),forest.isVisible((1,1)),forest.isVisible((1,2)),forest.isVisible((1,3)),forest.isVisible((0,0)))
# print(forest.isVisible((2,0)),forest.isVisible((2,1)),forest.isVisible((2,2)),forest.isVisible((2,3)),forest.isVisible((0,0)))
# print(forest.isVisible((3,0)),forest.isVisible((3,1)),forest.isVisible((3,2)),forest.isVisible((3,3)),forest.isVisible((0,0)))
# print(forest.isVisible((4,0)),forest.isVisible((4,1)),forest.isVisible((4,2)),forest.isVisible((4,3)),forest.isVisible((0,0)))


# PART 1
# total = 0
# # print(forest.getLength(), forest.getHeight())
# for x in range(forest.getLength()):
#     for y in range(forest.getHeight()):
#         if forest.isVisible((x,y)):
#             total += 1
# print(total)

scores = []

for x in range(forest.getLength()):
    for y in range(forest.getHeight()):
        scores.append(forest.getScenicScore((x,y)))

print(max(scores))