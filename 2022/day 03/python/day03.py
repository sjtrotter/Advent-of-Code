#!/usr/bin/env python

lettervalues = {}

theletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", \
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", \
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", \
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

value = 1
for letter in theletters:
    lettervalues[letter] = value
    value += 1

# print(lettervalues)
# exit()

inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

values =[]
marker = 0
elfgroup = {}
for line in data_list:
    # half1 = line[:int(len(line)/2)] # for pt1
    # half2 = line[int(len(line)/2):] # for pt1
    elfgroup[marker] = line

    if (marker == 2):
        for letter in elfgroup[0]:
            if (letter in elfgroup[1] and letter in elfgroup[2]):
                values.append(lettervalues[letter])
                break
    # for letter in half1: # for pt1
    #     if (letter in half2):
    #         # print(letter, lettervalues[letter])
    #         values.append(lettervalues[letter])
    #         break
    marker += 1
    if marker == 3: marker = 0

print(values)
print(sum(values))