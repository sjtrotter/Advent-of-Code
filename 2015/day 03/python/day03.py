import argparse

DEBUG = False

def parse_input(input_data):
    # DEFINE CUSTOM PARSING HERE
    ...


def debug_print(msg):
    # Use ANSI escape codes to set the text color to yellow
    global DEBUG
    if DEBUG:
        print('\033[33m[+]\033[0m', msg)

def deliverPresent(x,y,grid):
    if not (x,y) in grid.keys():
        grid[(x,y)] = 1
    else:
        grid[(x,y)] += 1



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
    # data = parse_input(input_data) # Customize to problem

    grid = {}

    x = 0
    y = 0

    for direction in input_data:

        deliverPresent(x,y,grid)
        if direction == ">":
            x += 1
        if direction == "<":
            x -= 1
        if direction == "^":
            y -= 1
        if direction == "v":
            y += 1
        deliverPresent(x,y,grid)

    print("part1:",len(grid.keys()))

    grid = {}
    x = 0
    y = 0

    for i in range(0,len(input_data),2):
        deliverPresent(x,y,grid)
        if input_data[i] == ">":
            x += 1
        if input_data[i] == "<":
            x -= 1
        if input_data[i] == "^":
            y -= 1
        if input_data[i] == "v":
            y += 1
        deliverPresent(x,y,grid)

    x = 0
    y = 0

    for i in range(1,len(input_data),2):
        deliverPresent(x,y,grid)
        if input_data[i] == ">":
            x += 1
        if input_data[i] == "<":
            x -= 1
        if input_data[i] == "^":
            y -= 1
        if input_data[i] == "v":
            y += 1
        deliverPresent(x,y,grid)

    print("part2:",len(grid.keys()))


if __name__ == '__main__':
    main()