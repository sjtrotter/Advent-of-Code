import argparse

DEBUG = False

def parse_input(input_data):
    # DEFINE CUSTOM PARSING HERE
    strings = [line.strip('"') for line in input_data.split('\n')]

    return strings

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
        # debug_print(f'Read input from {args.input_file}: {input_data}')


    # CODE REST OF PROBLEM MAINLOOP HERE
    strings = parse_input(input_data)

    memorySize = 0
    codeSize = 0
    for s in strings:
        # Parse the string as a regular string
        regular_length = len(s)
        print(f"Length of regular string '{s}': {regular_length}")

        # Parse the string as a raw string
        raw_length = len(r"{s}")
        print(f"Length of raw string '{s}': {raw_length}\n")
        
        memorySize += regular_length
        codeSize += raw_length

    debug_print(str(codeSize)+" - "+str(memorySize))
    print("part1:",codeSize-memorySize)
    


if __name__ == '__main__':
    main()