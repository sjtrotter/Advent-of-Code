import argparse
from itertools import permutations

DEBUG = False

def parse_input(input_data):
    # DEFINE CUSTOM PARSING HERE
    distances = [line.strip() for line in input_data.split('\n')]

    cityDistances = {}
    for line in distances:
        if line == "": break
        parts = line.split(" ")
        if not parts[0] in cityDistances.keys():
            cityDistances[parts[0]] = {}
        if not parts[2] in cityDistances.keys():
            cityDistances[parts[2]] = {}

        cityDistances[parts[0]][parts[2]] = int(parts[-1])
        cityDistances[parts[2]][parts[0]] = int(parts[-1])

    return cityDistances

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
        debug_print(f'Read input from {args.input_file}: \n{input_data}')


    # CODE REST OF PROBLEM MAINLOOP HERE
    cityDistances = parse_input(input_data) # Customize to problem

    debug_print(cityDistances)
    locations = list(cityDistances.keys())
    shortest = float("inf")
    shortpath = []

    for city in cityDistances.keys():
        destinations = list(cityDistances.keys())
        destinations.pop(destinations.index(city))
        perms = list(permutations(destinations))
        debug_print(city+" - "+str(perms))
        for perm in perms:
            path = [city]
            distance = cityDistances[city][perm[0]]
            path.append(perm[0])
            for i in range(1,len(perm)):
                distance += cityDistances[perm[i-1]][perm[i]]
                path.append(perm[i])
            debug_print(path)
            if distance < shortest:
                shortest = distance
                shortpath = path

    print("part1:",shortest," - ",shortpath)


    locations = list(cityDistances.keys())
    longest = 0
    longpath = []

    for city in cityDistances.keys():
        destinations = list(cityDistances.keys())
        destinations.pop(destinations.index(city))
        perms = list(permutations(destinations))
        debug_print(city+" - "+str(perms))
        for perm in perms:
            path = [city]
            distance = cityDistances[city][perm[0]]
            path.append(perm[0])
            for i in range(1,len(perm)):
                distance += cityDistances[perm[i-1]][perm[i]]
                path.append(perm[i])
            debug_print(path)
            if distance > longest:
                longest = distance
                longpath = path

    print("part2:",longest," - ",longpath)

if __name__ == '__main__':
    main()