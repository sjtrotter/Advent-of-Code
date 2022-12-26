class Rock:
    def __init__(self, pos, shape):
        self.pos = pos # pos is always lower left
        self.shape = shape
        
    def pixels(self, pos):
        x, y = pos
        if self.shape == 0:
            return (x, y), (x+1, y), (x+2, y), (x+3, y)
        if self.shape == 1:
            return (x+1, y), (x, y+1), (x+1, y+1), (x+2, y+1), (x+1, y+2)
        if self.shape == 2:
            return (x, y), (x+1, y), (x+2, y), (x+2, y+1), (x+2, y+2)
        if self.shape == 3:
            return (x, y), (x, y+1), (x, y+2), (x, y+3)
        return (x, y), (x+1, y), (x, y+1), (x+1, y+1)
    
    def move(self, direction='v'):
        x, y = self.pos
        if direction == '<':
            self.pos = (x-1, y)
        elif direction == '>':
            self.pos = (x+1, y)
        else:
            self.pos = (x, y-1)
            
class Tetris:
    def __init__(self):
        self.blocked = set()
        for x in range(7):
            self.blocked.add((x, 0))
        self.rocksLanded = 0
        self.addRock()
            
    def canMove(self, direction):
        dirs = {'<': (-1, 0), '>': (1, 0), 'v': (0, -1)}
        rx, ry = self.current.pos
        dx, dy = dirs[direction]
        for x, y in self.current.pixels((rx+dx, ry+dy)):
            if x < 0 or x > 6 or (x, y) in self.blocked:
                return False
        return True
    
    def moveRock(self, direction):
        self.current.move(direction)
        
    def addRock(self, shape = 0):
        yMax = max(p[1] for p in self.blocked)
        self.current = Rock((2, yMax+4), shape)
        
    def landRock(self):
        shape = (self.current.shape + 1) % 5
        for p in self.current.pixels(self.current.pos):
            self.blocked.add(p)
        self.rocksLanded += 1
        self.addRock(shape)
        
    def asString(self): # for visualization
        res = ['+-------+']
        pixels = self.current.pixels(self.current.pos)
        yMax = max(p[1] for p in pixels)
        for y in range(1, yMax):
            s = '|'
            for x in range(7):
                if (x, y) in self.blocked:
                    s += '#'
                elif (x, y) in pixels:
                    s += '@'
                else:
                    s += '.'
            s += '|'
            res.append(s)
        return res
    
    def asHash(self, moveIndex):
        yMax = max(p[1] for p in game.blocked)
        diffs = []
        for i in range(7):
            d = min(yMax - x[1] for x in self.blocked if x[0] == i)
            diffs.append(d)
        heights = tuple(diffs)
        return (moveIndex, self.current.shape, heights)

with open('input.txt') as f:
    items = list(map(str.strip, f.readlines()))
    
jets = items[0]
i = 0
game = Tetris()

while game.rocksLanded < 2022:
    move = jets[i]
    if game.canMove(move):
        game.moveRock(move)
    if game.canMove('v'):
        game.moveRock('v')
    else:
        game.landRock()
        
    i = (i + 1) % len(jets)
    
yMax = max(p[1] for p in game.blocked)
print(yMax)

hashes = []
i = 0
game = Tetris()
hashVals = {}

while True:
    h = game.asHash(i)
    if h in hashes:
        break
    hashes.append(h)
    hashVals[h] = (game.rocksLanded, max(p[1] for p in game.blocked))
    move = jets[i]
    if game.canMove(move):
        game.moveRock(move)
    if game.canMove('v'):
        game.moveRock('v')
    else:
        game.landRock()
    i = (i + 1) % len(jets)
    
curH = max(p[1] for p in game.blocked)
curL = game.rocksLanded
rocksPerCycle = curL-hashVals[h][0]
heightPerCycle = curH-hashVals[h][1]
totRocks = 1_000_000_000_000
completeCycles = (totRocks - curL) // rocksPerCycle
left = totRocks - curL - rocksPerCycle * completeCycles

game.rocksLanded = 0
while game.rocksLanded < left:
    move = jets[i]
    if game.canMove(move):
        game.moveRock(move)
    if game.canMove('v'):
        game.moveRock('v')
    else:
        game.landRock()
    i = (i + 1) % len(jets)
    
totHeight = max(p[1] for p in game.blocked) + heightPerCycle * completeCycles
print(totHeight)