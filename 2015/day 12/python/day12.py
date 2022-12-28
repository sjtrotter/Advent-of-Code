import argparse
import json

# got some help from reddit for this:
# https://www.reddit.com/r/adventofcode/comments/3wh73d/comment/cxw7ogw/?utm_source=share&utm_medium=web2x&context=3
# https://www.reddit.com/r/adventofcode/comments/3wh73d/comment/cy0zvlc/?utm_source=share&utm_medium=web2x&context=3

DEBUG = False

def parse_input(input_data):
    # DEFINE CUSTOM PARSING HERE
    return json.loads(input_data)


def debug_print(msg):
    # Use ANSI escape codes to set the text color to yellow
    global DEBUG
    if DEBUG:
        print('\033[33m[+]\033[0m', msg)


def sum_numbers(obj):
    if type(obj) == type(dict()):
        return sum(map(sum_numbers, obj.values()))

    if type(obj) == type(list()):
        return sum(map(sum_numbers, obj))

    if type(obj) == type(0):
        return obj

    return 0

def sumObject(obj):
    if type(obj) is int:
        return obj
    
    if type(obj) is list:
        return sum(map(sumObject, obj))
    
    if type(obj) is dict:
        vals = obj.values()
        if "red" in vals:
            return 0
        
        return sum(map(sumObject, vals))
    
    else:
        return 0


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
    debug_print(type(data))
    sum = sum_numbers(data)

    print("part1:",sum)

    sum = sumObject(data)

    print("part2:",sum)

if __name__ == '__main__':
    main()