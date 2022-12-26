#!/usr/bin/env python

elf = { "A": "rock",
        "B": "paper",
        "C": "scissors" }

you = { "X": "lose",
        "Y": "draw",
        "Z": "win" }

def win(elf, you):
    result = ""
    if (elf == "rock"):
        if (you == "draw"):
            result = "rock"
        elif (you == "win"):
            result = "paper"
        elif (you == "lose"):
            result = "scissors"
    elif (elf == "paper"):
        if (you == "lose"):
            result = "rock"
        elif (you == "draw"):
            result = "paper"
        elif (you == "win"):
            result = "scissors"
    elif (elf == "scissors"):
        if (you == "win"):
            result = "rock"
        elif (you == "lose"):
            result = "paper"
        elif (you == "draw"):
            result = "scissors"
    return result

def svalue(shape):
    if (shape == "rock"):
        return 1
    elif (shape == "paper"):
        return 2
    elif (shape == "scissors"):
        return 3
    
def wvalue(result):
    if (result == "draw"):
        return 3
    elif (result == "lose"):
        return 0
    elif (result == "win"):
        return 6

inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

results = []
for line in data_list:
    a, b = line.split(" ")
    a = elf[a]
    b = you[b]
    shape = win(a, b)
    winvalue = wvalue(b)
    shapevalue = svalue(shape)
    # print("winvalue", winvalue)
    # print("shapevalue", shapevalue)
    results.append(winvalue + shapevalue)

print(results)
print(sum(results))