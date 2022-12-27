import argparse

DEBUG = False

def parse_input(input_data):
    # DEFINE CUSTOM PARSING HERE
    data = [line.strip() for line in input_data.split('\n')]

    return data


def debug_print(msg):
    # Use ANSI escape codes to set the text color to yellow
    global DEBUG
    if DEBUG:
        print('\033[33m[+]\033[0m', msg)


def naughtyOrNice(string):
    # Check for auto-naughty
    if "ab" in string or "cd" in string or "pq" in string or "xy" in string:
        return False
    # check for 3x vowels of any type
    vowels = 0
    for letter in "aeiou":
        for char in string:
            if char in letter:
                vowels += 1
    if vowels < 3:
        return False
    # check for double letters of any type (return right away if one found)
    double = 0
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter*2 in string:
            return True
    # return false if not yet returned.
    return False


def double(string):
    for i in range(len(string)-3):
        double = string[i:i+2]
        if double in string[i+2:]:
            return True
    return False

def oneLetterBetween(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False


def naughtyOrNice2(string):
    # got help from https://www.reddit.com/r/adventofcode/comments/3viazx/comment/cxnswjz/?utm_source=share&utm_medium=web2x&context=3
    # for the logic here, I was overcomplicating.
    if not double(string):
        return False
    if not oneLetterBetween(string):
        return False
    return True


    

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

    nice = 0
    for line in data:
        if naughtyOrNice(line):
            nice += 1

    print("part1:",nice)

    nice = 0
    for line in data:
        if naughtyOrNice2(line):
            nice += 1

    print("part2:",nice)

if __name__ == '__main__':
    main()