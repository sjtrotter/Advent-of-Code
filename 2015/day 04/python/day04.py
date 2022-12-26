import argparse
import hashlib

DEBUG = False

def parse_input(input_data):
    # DEFINE CUSTOM PARSING HERE
    ...


def debug_print(msg):
    # Use ANSI escape codes to set the text color to yellow
    global DEBUG
    if DEBUG:
        print('\033[33m[+]\033[0m', msg)

def crypto(check, input_data):
    number = 0
    done = False
    while not done:
        number += 1
        string = input_data + str(number)
        md5 = hashlib.md5(string.encode())
        debug_print(string + " - " + str(md5.hexdigest()))
        if md5.hexdigest()[:check] == "0" * check:
            done = True

    return number

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
            input_data = f.read().strip()
        debug_print(f'Read input from {args.input_file}: {input_data}')


    # CODE REST OF PROBLEM MAINLOOP HERE
    # data = parse_input(input_data) # Customize to problem

    print("part1:",crypto(5,input_data))
    print("part2:",crypto(6,input_data))


if __name__ == '__main__':
    main()