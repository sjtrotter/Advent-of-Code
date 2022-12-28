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

def lookAndSay(a):
    # had this working but it was taking a LOOONG time.
    # CHAT GPT refined the function to this:
    result = []
    i = 0
    while i < len(a):
        char = a[i]
        count = 1
        for j in range(i+1, len(a)):
            if a[j] != char:
                break
            count += 1
        result.append(str(count) + char)
        i += count
    return ''.join(result)


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
        debug_print(f'Read input from {args.input_file}: \n{input_data}')


    # CODE REST OF PROBLEM MAINLOOP HERE
    # data = parse_input(input_data) # Customize to problem

    input = input_data
    debug_print(lookAndSay(input_data))
    # debug_print(lookAndSay("1211"))
    for i in range(40):
        input = lookAndSay(input)
        # debug_print(input)

    print("part1:",len(input))

    input = input_data
    for i in range(50):
        input = lookAndSay(input)

    print("part2:",len(input))

if __name__ == '__main__':
    main()