import argparse

DEBUG = False

def parse_input(input_data):
    # DEFINE CUSTOM PARSING HERE
    data = [line.strip() for line in input_data.split('\n')]
    instr = []
    for line in data:
        newline = line.split(" through ")
        debug_print(newline)
        t_x = int(newline[-1].split(",")[0].strip())
        t_y = int(newline[-1].split(",")[1].strip())
        f_x = int(newline[0].split(" ")[-1].split(",")[0])
        f_y = int(newline[0].split(" ")[-1].split(",")[1])
        cmd = newline[0].split(" ")[-2]
        instr.append((cmd,(f_x,f_y),(t_x,t_y)))

    return instr

def debug_print(msg):
    # Use ANSI escape codes to set the text color to yellow
    global DEBUG
    if DEBUG:
        print('\033[33m[+]\033[0m', msg)


def turn_off(fr, to, grid):
    for y in range(fr[1],to[1]+1):
        for x in range(fr[0],to[0]+1):
            if (x,y) in grid.keys():
                del(grid[(x,y)])

    return grid


def turn_on(fr, to, grid):
    for y in range(fr[1],to[1]+1):
        for x in range(fr[0],to[0]+1):
            grid[(x,y)] = 1

    return grid


def toggle(fr, to, grid):
    for y in range(fr[1],to[1]+1):
        for x in range(fr[0],to[0]+1):
            if (x,y) in grid.keys():
                del(grid[(x,y)])
            else:
                grid[(x,y)] = 1

    return grid


def turn_off2(fr, to, grid):
    for y in range(fr[1],to[1]+1):
        for x in range(fr[0],to[0]+1):
            if (x,y) in grid.keys():
                if grid[(x,y)] > 0:
                    grid[(x,y)] -= 1

    return grid


def turn_on2(fr, to, grid):
    for y in range(fr[1],to[1]+1):
        for x in range(fr[0],to[0]+1):
            grid[(x,y)] += 1

    return grid


def toggle2(fr, to, grid):
    for y in range(fr[1],to[1]+1):
        for x in range(fr[0],to[0]+1):
            grid[(x,y)] += 2

    return grid


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
    debug_print(data)

    grid = {}

    for instr in data:
        cmd, fr, to = instr
        if cmd == "on":
            grid = turn_on(fr, to, grid)
        elif cmd == "off":
            grid = turn_off(fr, to, grid)
        elif cmd == "toggle":
            grid = toggle(fr, to, grid)
    
    debug_print(grid)
    print("part1:",len(grid.keys()))

    for y in range(1000):
        for x in range(1000):
            grid[(x,y)] = 0

    for instr in data:
        cmd, fr, to = instr
        if cmd == "on":
            turn_on2(fr, to, grid)
        elif cmd == "off":
            turn_off2(fr, to, grid)
        elif cmd == "toggle":
            toggle2(fr, to, grid)

    total = list(grid.values())
    print("part2:", sum(total))


if __name__ == '__main__':
    main()