"""
Chat GPT's first solution didn't work, so I started parsing data.
I restarted Chat GPT after, and gave it the input, which it was able to solve with.
"""

import argparse

DEBUG = False

def parse_input(input_data):
    # DEFINE CUSTOM PARSING HERE
    data = input_data.strip("\n").split("\n")
    ingredients = {}
    for line in data:
        ingredient, _, capacity, _, durability, _, flavor, _, texture, _, calories = line.split()
        ingredient = ingredient.strip(":")
        durability = int(durability.strip(","))
        flavor = int(flavor.strip(","))
        texture = int(texture.strip(","))
        calories = int(calories.strip(","))

        ingredients[ingredient] = {
            "capacity": capacity,
            "durability": durability,
            "flavor": flavor,
            "texture": texture,
            "calories": calories
        }

    return ingredients


def debug_print(msg):
    # Use ANSI escape codes to set the text color to yellow
    global DEBUG
    if DEBUG:
        print('\033[33m[+]\033[0m', msg)


def main():
    global DEBUG
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process some input.')
    parser.add_argument('--debug', action='store_true', help='enable debug messages')
    parser.add_argument('input_file', help='input file')
    
    # Parse command-line arguments
    args = parser.parse_args()
    
    # Print debug messages if --debug flag is set
    if args.debug:
        DEBUG = True
        debug_print('Debug mode enabled')
    
    # Read input file if --input flag is set
    if args.input_file:
        with open(args.input_file, 'r') as f:
            input_data = f.read()
        debug_print(f'Read input from {args.input_file}: {input_data}')


    # CODE REST OF PROBLEM MAINLOOP HERE
    data = parse_input(input_data) # Customize to problem
    print(data)



if __name__ == '__main__':
    main()