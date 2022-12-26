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


def upOrDown(instr):
    if instr == "(":
        return 1
    elif instr == ")":
        return -1


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



    floor = 0
    for instr in input_data:
        floor += upOrDown(instr)

    print("part1:",floor)

    floor = 0
    for index in range(1,len(input_data)+1):
        debug_print(str(index-1)+" - "+input_data[index-1]+"floor "+str(floor))
        floor += upOrDown(input_data[index-1])
        if floor < 0:
            break
    
    print("part2:",index)




if __name__ == '__main__':
    main()