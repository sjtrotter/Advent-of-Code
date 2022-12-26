from functools import cmp_to_key
import json

with open('input.txt') as inputfile:
    data = inputfile.read()

pairs = [pair.split('\n') for pair in data.split('\n\n')]

def isInOrder(a, b):
    maxLen = max(len(a), len(b))
    for index in range(maxLen):
        if index == len(a) and index < len(b):
            return True
        if index < len(a) and index == len(b):
            return False      

        aval = a[index]
        bval = b[index]
        if isinstance(aval, int) and isinstance(bval, int):
            if aval < bval:
                return True
            if aval > bval:
                return False
        elif isinstance(aval, list) and isinstance(bval, list):
            result = isInOrder(aval, bval)
            if result is not None:
                return result
        elif isinstance(aval, int) and isinstance(bval, list):
            result = isInOrder([aval], bval)
            if result is not None:
                return result
        elif isinstance(aval, list) and isinstance(bval, int):
            result = isInOrder(aval, [bval])
            if result is not None:
                return result
    
    return None

inorder = 0
for pairNo, pair in enumerate(pairs):
    a = eval(pair[0])
    b = eval(pair[1])
    if isInOrder(a, b):
        inorder += pairNo + 1

print(f'part 1: {inorder}')

# part 2

lines = [line.strip() for line in data.replace('\n\n', '\n').split('\n')]
print(lines)
print()
lines.append('[[2]]')
lines.append('[[6]]')
packets = []
for line in lines:
    print(line)
    packets.append(json.loads(line))
sortedPackets = sorted(packets, key = cmp_to_key(lambda a, b: -1 if isInOrder(a,b) else 1))
index2 = sortedPackets.index([[2]]) + 1
index6 = sortedPackets.index([[6]]) + 1

print(f'part 2: {index2 * index6}')
