class Reindeer:
    def __init__(self, name, speed, flight_time, rest_time):
        self.name = name
        self.speed = speed
        self.flight_time = flight_time
        self.rest_time = rest_time
        self.distance = 0
        self.points = 0
        self.state = "flying"
        self.time_in_state = 0
    
    def update(self):
        if self.state == "flying":
            self.distance += self.speed
            self.time_in_state += 1
            if self.time_in_state == self.flight_time:
                self.state = "resting"
                self.time_in_state = 0
        else:
            self.time_in_state += 1
            if self.time_in_state == self.rest_time:
                self.state = "flying"
                self.time_in_state = 0

# Read the input and create the list of reindeer
reindeer = []
with open("../input.txt") as f:
    for line in f:
        name, _, _, speed, _, _, flight_time, _, _, _, _, _, _, rest_time, _ = line.strip().split()
        speed = int(speed)
        flight_time = int(flight_time)
        rest_time = int(rest_time)
        reindeer.append(Reindeer(name, speed, flight_time, rest_time))

# Simulate the race for the given number of seconds
for t in range(1, 2504):
    # Update the distance traveled by each reindeer
    for r in reindeer:
        r.update()
    # Determine the maximum distance traveled
    max_distance = max(r.distance for r in reindeer)
    # Award one point to each reindeer with the maximum distance
    for r in reindeer:
        if r.distance == max_distance:
            r.points += 1

# Print the maximum distance traveled
print(max_distance)
# Print the points earned by the winning reindeer
print(max(r.points for r in reindeer))