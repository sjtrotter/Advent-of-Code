import time
from copy import deepcopy

#Timing: Start
start = time.perf_counter()

#Monkey Class
class Monkey():

    def __init__(self, items: list, operator: str, operand: str, 
                 divisor: int, true_monkey: int, false_monkey: int):
        self.items = items
        self.operator = operator
        if operand == 'old':
            self.operand = -1
        else:
            self.operand = int(operand)
        self.divisor = divisor
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspections = 0
        self.lcm = 0

    def ExamineItems(self, monkeys: list, part1: bool):
        self.inspections += len(self.items)
        true_monkeys = monkeys[self.true_monkey].items
        false_monkeys = monkeys[self.false_monkey].items
        while len(self.items):
            current_item = self.items.pop(0)
            if self.operator == '+':
                current_item += self.operand
            else:
                if self.operand == -1:
                    current_item *= current_item
                else:
                    current_item *= self.operand
            if part1:
                current_item = current_item // 3
            else:
                current_item = current_item % self.lcm
            if (current_item % self.divisor) == 0:
                true_monkeys.append(current_item)
            else:
                false_monkeys.append(current_item)

#Load the puzzle data
with open('input.txt') as f:
    data = [line.rstrip() for line in f.readlines()]
groups = []
temp = []
for line in data:
    if line == '':
        if len(temp):
            groups.append(temp)
            temp = []
    else:
        temp.append(line)
if len(temp):
    groups.append(temp)
              
#Load data into Monkey objects
p1_monkeys = []
divisors = []
for monkey in groups:
    items = [int(x) for x in monkey[1].replace(',', ' ').split()[2:]]
    ops = monkey[2].split()
    operator = ops[4]
    operand = ops[5]
    divisor = int(monkey[3].split()[3])
    divisors.append(divisor)
    true_monkey = int(monkey[4].split()[5])
    false_monkey = int(monkey[5].split()[5])
    p1_monkeys.append(Monkey(items, operator, operand, divisor, true_monkey, false_monkey)) 

#Sort out LCM for Part 2
lcm = 1
for div in divisors:
    lcm *= div
for monkey in p1_monkeys:
    monkey.lcm = lcm

#Make a fresh copy for Part 2
p2_monkeys = deepcopy(p1_monkeys)

def solve(cycles, monkeys, part1):
    for n in range(cycles):
        for monkey in monkeys:
            monkey.ExamineItems(monkeys, part1)
    inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
    print(inspections[0] * inspections[1])

#Part 1
solve(20, p1_monkeys, True)

#Part 2
solve(10000, p2_monkeys, False)

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
