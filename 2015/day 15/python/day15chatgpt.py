import itertools

# Set up the ingredients and their properties
ingredients = [
    ("Sprinkles", 2, 0, -2, 0, 3),
    ("Butterscotch", 0, 5, -3, 0, 3),
    ("Chocolate", 0, 0, 5, -1, 8),
    ("Candy", 0, -1, 0, 5, 8),
]

# Set the number of teaspoons of each ingredient that we can use
teaspoons = 100

# Set the maximum score to 0
max_score = 0

# Set the maximum scoring combination to an empty list
max_combo = []

# Iterate over all possible combinations of ingredients
for combo in itertools.combinations_with_replacement(ingredients, teaspoons):
    # Calculate the total score for this combination
    capacity = sum(i[1] for i in combo)
    durability = sum(i[2] for i in combo)
    flavor = sum(i[3] for i in combo)
    texture = sum(i[4] for i in combo)
    
    # Make sure all properties are non-negative
    if capacity < 0:
        capacity = 0
    if durability < 0:
        durability = 0
    if flavor < 0:
        flavor = 0
    if texture < 0:
        texture = 0
    
    # Calculate the total score for this combination
    total_score = capacity * durability * flavor * texture
    
    # Update the maximum score and maximum scoring combination if necessary
    if total_score > max_score:
        max_score = total_score
        max_combo = combo

# Print the maximum score and the corresponding combination of ingredients
print(f"part1: {max_score}")

# Set the maximum score to 0
max_score = 0

# Set the maximum scoring combination to an empty list
max_combo = []

for combo in itertools.combinations_with_replacement(ingredients, teaspoons):
    # Calculate the total score for this combination
    capacity = sum(i[1] for i in combo)
    durability = sum(i[2] for i in combo)
    flavor = sum(i[3] for i in combo)
    texture = sum(i[4] for i in combo)
    calories = sum(i[5] for i in combo)
    
    # Make sure all properties are non-negative and the total number of calories is 500
    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0 or calories != 500:
        continue
    
    # Calculate the total score for this combination
    total_score = capacity * durability * flavor * texture
    
    # Update the maximum score and maximum scoring combination if necessary
    if total_score > max_score:
        max_score = total_score
        max_combo = combo

# Print the maximum score and the corresponding combination of ingredients
print(f"part2: {max_score}")
