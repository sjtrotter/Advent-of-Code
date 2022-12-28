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



def meetsRequirements(password):
    hasStraight = False
    for i in range(len(password)-3):
        if ord(password[i]) + 1 == ord(password[i+1]) and \
            ord(password[i+1]) + 1 == ord(password[i+2]):
            hasStraight = True
            break
    
    if not hasStraight: debug_print("failed, no straight: "+password); return False
    else: debug_print(password+" has a straight")

    hasForbidden = "i" in password or "o" in password or "l" in password
    if hasForbidden: debug_print("failed, has forbidden chars: "+password); return False
    else: debug_print(password+" has no forbidden chars")

    hasDoubles = False
    doubles = 0
    check=" "
    for i in range(len(password)-1):
        if password[i] == password[i+1] and check != password[i]:
            check = password[i]
            i += 1
            doubles += 1
            if doubles > 1: hasDoubles = True; break

    if not hasDoubles: debug_print("failed, not enuf doubles: "+password); return False
    else: debug_print(password+" has a double")

    return hasStraight and not hasForbidden and hasDoubles

def increment(password):
    debug_print("incrementing: "+password)
    done = False
    p = list(password)
    i = len(p) - 1
    while not done:
        if i == -1: break
        char = p[i]
        if char == "z":
            p[i] = "a"
            i -= 1
        else:
            p[i] = chr(ord(char) + 1)
            break

    return "".join(p)


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

    debug_print(input_data)
    debug_print(meetsRequirements(input_data))
    password = input_data
    while not meetsRequirements(password):
        password = increment(password)
        debug_print(password)

    print("part1:",password)


    password = increment(password)
    while not meetsRequirements(password):
        password = increment(password)

    print("part2:",password)

if __name__ == '__main__':
    main()