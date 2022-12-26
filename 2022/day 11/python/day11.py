#!/usr/bin/env python
import gmpy2
from gmpy2 import mpz,f_mod,add,mul,div


inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())

class Monkey():

    def __init__(self, items, operation, operand, test, true, false):

        self.items = items
        self.operation = operation
        self.operand = operand
        self.test = mpz(test)
        self.true = true
        self.false = false
        self.inspected = 0


    def inspect(self,item):
        # print("inspecting",item)
        self.inspected += 1
        item = self.oper(item)
        # item = int(item / 3)
        if self.testItem(item):
            self.throw(item, self.true)
            # print("throwing to",self.true)
        else:
            self.throw(item, self.false)
            # print("throwing to",self.false)
        

    def testItem(self, item):
        # if item % self.test == 0:
            # print("item",item,"is divisible by", self.test)
        # else:
            # print("item",item,"is not divisible by", self.test)
        return (f_mod(item,self.test) == 0)


    def throw(self, item, monkey):
        monkeys[monkey].catch(item)


    def catch(self, item):
        self.items.append(item)


    def oper(self, item):
        if self.operand == "old":
            operand = item
        else:
            operand = int(self.operand)
        
        if self.operation == "+":
            return add(item,operand)
        elif self.operation == "*":
            return mul(item,operand)
        else:
            print("error:",self,"operation is neither + nor *")
            exit()



monkeys = {}
monkeydata = {}
currentMonkey = 0
for line in data_list:
    if line.startswith("Monkey"):
        currentMonkey = line.split(":")[0].split(" ")[1]
        monkeydata[currentMonkey] = []
        # print(monkeyNumber)
    elif line.startswith("Starting"):
        newline = line.split(":")[1]
        itemlist = newline.split(",")
        for i in range(len(itemlist)):
            itemlist[i] = mpz(itemlist[i])
        monkeydata[currentMonkey].append(itemlist)
    elif line.startswith("Operation"):
        newline = line.split("=")[1]
        if "+" in newline:
            monkeydata[currentMonkey].append("+")
            monkeydata[currentMonkey].append(newline.split("+")[1].strip())
        elif "*" in newline:
            monkeydata[currentMonkey].append("*")
            monkeydata[currentMonkey].append(newline.split("*")[1].strip())
    elif line.startswith("Test"):
        monkeydata[currentMonkey].append(line.split(" ")[-1])
    elif line.startswith("If"):
        monkeydata[currentMonkey].append(line.split(" ")[-1])

# print(monkeydata)


for monkey in monkeydata.keys():
    monkeys[monkey] = Monkey(monkeydata[monkey][0],monkeydata[monkey][1], \
        monkeydata[monkey][2],monkeydata[monkey][3],monkeydata[monkey][4], \
            monkeydata[monkey][5])

# print(monkeys)


monkeyRound = 0
while monkeyRound < 10000:
    # for monkey in monkeys.keys():
        # print("Monkey", monkey,":",monkeys[monkey].items)
    monkeyRound += 1
    print(monkeyRound)
    for monkey in monkeys.keys():
        theItems = monkeys[monkey].items
        monkeys[monkey].items = []
        for item in theItems:
            monkeys[monkey].inspect(item)


# for monkey in monkeys.keys():
#     print("Monkey", monkey,":",monkeys[monkey].items)

inspectScores = []
for monkey in monkeys.keys():
    inspectScores.append(monkeys[monkey].inspected)

print(inspectScores)

inspectScores.sort()

print("part1:", inspectScores[-1] * inspectScores[-2])


# monkey0 = Monkey([79,98],"*",19,"/",23,2,3)

