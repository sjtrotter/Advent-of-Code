#!/usr/bin/env python

inputfile = open("input.txt", "r")
data = inputfile.readlines()
inputfile.close()

data_list = []
for line in data:
    data_list.append(line.strip())


monkeys = {}
for line in data_list:
    monkey,op = line.split(":")
    if monkey not in monkeys.keys():
        op = op.strip()
        if op.isnumeric():
            monkeys[monkey] = int(op)

def part1():
    # monkeys = {}
    done = False
    while not done:
        monkeysNotDone = 0
        for line in data_list:
            monkey,op = line.split(":")
            if monkey not in monkeys.keys():
                monkeysNotDone += 1
                op = op.strip()
                if op.isnumeric():
                    monkeys[monkey] = int(op)
                else:
                    try:
                        m1,op,m2 = op.split(" ")
                    except:
                        print("error: ",op.split(" "))
                        exit()
                    if m1 in monkeys.keys() and m2 in monkeys.keys():
                        if op == "+":
                            monkeys[monkey] = monkeys[m1] + monkeys[m2]
                        if op == "-":
                            monkeys[monkey] = monkeys[m1] - monkeys[m2]
                        if op == "*":
                            monkeys[monkey] = monkeys[m1] * monkeys[m2]
                        if op == "/":
                            monkeys[monkey] = monkeys[m1] / monkeys[m2]
        done = (monkeysNotDone == 0)
    print(monkeys["zhfp"], "+", monkeys["hghd"])
    return int(monkeys["root"])

def part2(humn):
    # monkeys = {}
    monkeys["humn"] = humn
    done = False
    while not done:
        monkeysNotDone = 0
        for line in data_list:
            monkey,op = line.split(":")
            if monkey not in monkeys.keys():
                monkeysNotDone += 1
                op = op.strip()
                if op.isnumeric():
                    monkeys[monkey] = int(op)
                else:
                    try:
                        m1,op,m2 = op.split(" ")
                    except:
                        print("error: ",op.split(" "))
                        exit()
                    if m1 in monkeys.keys() and m2 in monkeys.keys():
                        if op == "+":
                            monkeys[monkey] = monkeys[m1] + monkeys[m2]
                        if op == "-":
                            monkeys[monkey] = monkeys[m1] - monkeys[m2]
                        if op == "*":
                            monkeys[monkey] = monkeys[m1] * monkeys[m2]
                        if op == "/":
                            monkeys[monkey] = monkeys[m1] / monkeys[m2]
                        if op == "=":
                            monkeys[monkey] = monkeys[m1] == monkeys[m2]
        done = (monkeysNotDone == 0)
    return monkeys["root"]

print(part1())
data_list[data_list.index("root: zhfp + hghd")] = "root: zhfp = hghd" # for input
# data_list[data_list.index("root: pppw + sjmn")] = "root: pppw = sjmn" # for test

monkeys = {}
for line in data_list:
    monkey,op = line.split(":")
    if monkey not in monkeys.keys():
        op = op.strip()
        if op.isnumeric():
            monkeys[monkey] = int(op)

# key = "humn"
# humnAffected = {}
# while key != "root":

#     for line in data_list:
#         monkey,op = line.split(":")
#         if key in op:
#             humnAffected[monkey] = op.strip()
#             key = monkey

# print(humnAffected)


# keys = ["hghd"]
# hghdAffected = {}
# done = False
# while done is not True:
#     affected = 0
#     try:
#         key = keys.pop()
#     except:
#         break
#     for line in data_list:
#         monkey,op = line.split(":")
#         if key == monkey:
#             hghdAffected[monkey] = op.strip()
#             affected += 1
#             try:
#                 m1,oper,m2 = op.strip().split(" ")
#                 keys.append(m1)
#                 keys.append(m2)
#             except:
#                 print("error - numeric?:",op)
#                 break
#                 # exit()
#     done = affected == 0

# print(hghdAffected)

# add = 0
# minus = 0
# times = 0
# divide = 0

# for key in humnAffected.keys():
#     if "+" in humnAffected[key]:
#         add += 1
#     if "-" in humnAffected[key]:
#         minus += 1
#     if "*" in humnAffected[key]:
#         times += 1
#     if "/" in humnAffected[key]:
#         divide += 1

# print("humn:",add,minus,times,divide)

# add = 0
# minus = 0
# times = 0
# divide = 0

# for key in hghdAffected.keys():
#     if "+" in hghdAffected[key]:
#         add += 1
#     if "-" in hghdAffected[key]:
#         minus += 1
#     if "*" in hghdAffected[key]:
#         times += 1
#     if "/" in hghdAffected[key]:
#         divide += 1

# print("hghd:",add,minus,times,divide)


# exit()




i = 3220993874139

while not part2(i):
    if i % 1000 == 0:
        print("not under",i)
    i += 1
print(i)
# print("not between", low, "and", high)