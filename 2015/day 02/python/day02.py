import argparse

DEBUG = False

def parse_input(input_data):
    # DEFINE CUSTOM PARSING HERE
    data = [line.strip() for line in input_data.split('\n')]
    lists = []
    for line in data:
        lists.append(line.split('x'))

    return lists
    

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
    debug_print(data)

    # data: list of l,w,h lists
    totalPaper = 0
    totalRibbon = 0
    for i in data:
        # debug_print(i)
        l,w,h = i
        l,w,h = int(l),int(w),int(h)
        x,y,z = int(l)*int(w), int(w)*int(h), int(h)*int(l)
        slack = min(x,y,z)
        ribbonLength = min(l+w,w+h,l+h)*2
        bowLength = l*w*h
        ribbonRequired = ribbonLength + bowLength
        paperRequired = 2*x + 2*y + 2*z + slack
        totalPaper += paperRequired
        totalRibbon += ribbonRequired

    print("part1:",totalPaper)
    print("part2:",totalRibbon)



if __name__ == '__main__':
    main()