import itertools

# open the file and read the capacities
with open('../input.txt', 'r') as f:
  capacities = [int(x) for x in f.readlines()]

# generate all combinations of the capacities
combinations = []
for i in range(1, len(capacities) + 1):
  combinations.extend(list(itertools.combinations(capacities, i)))

# count the number of combinations that add up to 150 liters
count = 0
for c in combinations:
  if sum(c) == 150:
    count += 1

print("part1:",count)


# open the file and read the capacities
with open('../input.txt', 'r') as f:
  capacities = [int(x) for x in f.readlines()]

# generate all combinations of the capacities
combinations = []
for i in range(1, len(capacities) + 1):
  combinations.extend(list(itertools.combinations(capacities, i)))

# count the number of combinations that add up to 150 liters
min_containers = float('inf')
count = 0
for c in combinations:
  if sum(c) == 150:
    if len(c) < min_containers:
      min_containers = len(c)
      count = 1
    elif len(c) == min_containers:
      count += 1

# print(min_containers)
print("part2:",count)
