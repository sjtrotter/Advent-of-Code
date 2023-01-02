""" This code was fully functional from ChatGPT from the start. """

from itertools import permutations

# read input from file
with open("../input.txt", "r") as f:
    lines = f.readlines()

# list of guests
guests = []

# happiness units gained or lost by sitting next to each other guest
happiness = {}

for line in lines:
    words = line.strip().split()
    guest1 = words[0]
    guest2 = words[-1][:-1]
    gain_loss = int(words[3]) if words[2] == "gain" else -int(words[3])
    happiness[(guest1, guest2)] = gain_loss
    if guest1 not in guests:
        guests.append(guest1)
    if guest2 not in guests:
        guests.append(guest2)

# find the optimal seating arrangement
max_happiness = float("-inf")
for perm in permutations(guests):
    total_happiness = 0
    for i in range(len(perm)):
        total_happiness += happiness[(perm[i], perm[(i+1)%len(perm)])]
        total_happiness += happiness[(perm[(i+1)%len(perm)], perm[i])]
    max_happiness = max(max_happiness, total_happiness)

print(max_happiness)

guests.append("Yourself")
for guest in guests:
    if guest != "Yourself":
        happiness[("Yourself", guest)] = 0
        happiness[(guest, "Yourself")] = 0

# find the optimal seating arrangement
max_happiness = float("-inf")
for perm in permutations(guests):
    total_happiness = 0
    for i in range(len(perm)):
        total_happiness += happiness[(perm[i], perm[(i+1)%len(perm)])]
        total_happiness += happiness[(perm[(i+1)%len(perm)], perm[i])]
    max_happiness = max(max_happiness, total_happiness)

print(max_happiness)