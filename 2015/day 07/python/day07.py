import argparse

DEBUG = False

def parse_input(input_data):
    # DEFINE CUSTOM PARSING HERE
    data = [line.strip() for line in input_data.split('\n')]

    instructions = {}
    for line in data:
        parts = line.split(" ")
        wire = parts.pop() # the wire at the end
        parts.pop() # get rid of the ->
        if len(parts) == 1:
            instructions[wire] = ("ASSIGN",parts[0])
        elif len(parts) == 2:
            instructions[wire] = ("NOT",parts[1])
        elif len(parts) == 3:
            instructions[wire] = (parts[1],parts[0],parts[2])
        else:
            print("malformed instruction:", line)
            exit(1)

    return instructions


def debug_print(msg):
    # Use ANSI escape codes to set the text color to yellow
    global DEBUG
    if DEBUG:
        print('\033[33m[+]\033[0m', msg)


def NOT(a):
    if str(a).isnumeric():
        return int(a) ^ 1
    else:
        return a


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
    instructions = parse_input(input_data) # Customize to problem

    # debug_print(instructions)
    
    wires = {}
    while instructions:
        for wire, instruction in list(instructions.items()):
            # print(wire, instruction)
            operation = instruction[0]

            if operation == "ASSIGN":
                value = instruction[1]
                if value.isdigit():
                    debug_print("Direct integer assignment: "+value+" to "+wire)
                    wires[wire] = int(value)
                    del instructions[wire]
                elif value in wires.keys():
                    debug_print("Assignment to other wire, known: "+value+":"+str(wires[value])+" to "+wire)
                    wires[wire] = wires[value]
                    del instructions[wire]
                else:
                    debug_print("Assignment to other wire, unknown: "+value+":"+str(instructions[value])+" to "+wire)
                    pass

            elif operation == "NOT":
                value = instruction[1]
                if value.isdigit():
                    debug_print("Direct NOT operation: NOT "+value+" to "+wire)
                    wires[wire] = ~int(value) & 0xffff
                    del instructions[wire]
                elif value in wires.keys():
                    debug_print("NOT operation from other wire: NOT "+value+"("+str(wires[value])+") to "+wire)
                    wires[wire] = ~wires[value] & 0xffff
                    del instructions[wire]
                else:
                    debug_print("NOT operation from other wire, unknown: "+value+":"+str(instructions[value])+" to "+wire)

            else:
                value1 = instruction[1]
                value2 = instruction[2]
                # debug_print(value1+", "+value2)
                if value1.isdigit() and value2.isdigit():
                    debug_print("Direct "+operation+" operation: "+value1+" "+operation+" "+value2+" to "+wire)
                    if operation == "AND":
                        wires[wire] = int(value1) & int(value2)
                        del instructions[wire]
                    elif operation == "OR":
                        wires[wire] = int(value1) | int(value2)
                        del instructions[wire]
                    elif operation == "LSHIFT":
                        wires[wire] = int(value1) << int(value2)
                        del instructions[wire]
                    elif operation == "RSHIFT":
                        wires[wire] = int(value1) >> int(value2)
                        del instructions[wire]
                    else:
                        debug_print("unknown operation: "+operation)
                        exit(1)

                elif value1.isdigit() and value2 in wires.keys():
                    debug_print(operation+" operation from other wire: "+value1+" "+operation+" "+value2+"("+str(wires[value2])+") to "+wire)
                    if operation == "AND":
                        wires[wire] = int(value1) & int(wires[value2])
                        del instructions[wire]
                    elif operation == "OR":
                        wires[wire] = int(value1) | int(wires[value2])
                        del instructions[wire]
                    elif operation == "LSHIFT":
                        wires[wire] = int(value1) << int(wires[value2])
                        del instructions[wire]
                    elif operation == "RSHIFT":
                        wires[wire] = int(value1) >> int(wires[value2])
                        del instructions[wire]
                    else:
                        debug_print("unknown operation: "+operation)
                        exit(1)

                elif value1 in wires.keys() and value2.isdigit():
                    debug_print(operation+" operation from other wire: "+value1+"("+str(wires[value1])+") "+operation+" "+value2+" to "+wire)
                    if operation == "AND":
                        wires[wire] = int(wires[value1]) & int(value2)
                        del instructions[wire]
                    elif operation == "OR":
                        wires[wire] = int(wires[value1]) | int(value2)
                        del instructions[wire]
                    elif operation == "LSHIFT":
                        wires[wire] = int(wires[value1]) << int(value2)
                        del instructions[wire]
                    elif operation == "RSHIFT":
                        wires[wire] = int(wires[value1]) >> int(value2)
                        del instructions[wire]
                    else:
                        debug_print("unknown operation: "+operation)
                        exit(1)
                    
                elif value1 in wires.keys() and value2 in wires.keys():
                    debug_print(operation+" operation from other wires: "+value1+"("+str(wires[value1])+") "+operation+" "+value2+"("+str(wires[value2])+") to "+wire)
                    if operation == "AND":
                        wires[wire] = int(wires[value1]) & int(wires[value2])
                        del instructions[wire]
                    elif operation == "OR":
                        wires[wire] = int(wires[value1]) | int(wires[value2])
                        del instructions[wire]
                    elif operation == "LSHIFT":
                        wires[wire] = int(wires[value1]) << int(wires[value2])
                        del instructions[wire]
                    elif operation == "RSHIFT":
                        wires[wire] = int(wires[value1]) >> int(wires[value2])
                        del instructions[wire]
                    else:
                        debug_print("unknown operation: "+operation)
                        exit(1)

                elif value1 not in wires.keys() or value2 in wires.keys():
                    # debug_print(operation+" operation from other wires: "+value1+str(instructions[value1])+" "+operation+" "+value2+"("+wires[value2]+") to "+wire)
                    pass

    # print(wires)
    print("part1:",wires["a"])

    instructions = parse_input(input_data) # Customize to problem
    instructions['b'] = ("ASSIGN",str(wires['a']))

    wires = {}
    while instructions:
        for wire, instruction in list(instructions.items()):
            # print(wire, instruction)
            operation = instruction[0]

            if operation == "ASSIGN":
                value = instruction[1]
                if value.isdigit():
                    debug_print("Direct integer assignment: "+value+" to "+wire)
                    wires[wire] = int(value)
                    del instructions[wire]
                elif value in wires.keys():
                    debug_print("Assignment to other wire, known: "+value+":"+str(wires[value])+" to "+wire)
                    wires[wire] = wires[value]
                    del instructions[wire]
                else:
                    debug_print("Assignment to other wire, unknown: "+value+":"+str(instructions[value])+" to "+wire)
                    pass

            elif operation == "NOT":
                value = instruction[1]
                if value.isdigit():
                    debug_print("Direct NOT operation: NOT "+value+" to "+wire)
                    wires[wire] = ~int(value) & 0xffff
                    del instructions[wire]
                elif value in wires.keys():
                    debug_print("NOT operation from other wire: NOT "+value+"("+str(wires[value])+") to "+wire)
                    wires[wire] = ~wires[value] & 0xffff
                    del instructions[wire]
                else:
                    debug_print("NOT operation from other wire, unknown: "+value+":"+str(instructions[value])+" to "+wire)

            else:
                value1 = instruction[1]
                value2 = instruction[2]
                # debug_print(value1+", "+value2)
                if value1.isdigit() and value2.isdigit():
                    debug_print("Direct "+operation+" operation: "+value1+" "+operation+" "+value2+" to "+wire)
                    if operation == "AND":
                        wires[wire] = int(value1) & int(value2)
                        del instructions[wire]
                    elif operation == "OR":
                        wires[wire] = int(value1) | int(value2)
                        del instructions[wire]
                    elif operation == "LSHIFT":
                        wires[wire] = int(value1) << int(value2)
                        del instructions[wire]
                    elif operation == "RSHIFT":
                        wires[wire] = int(value1) >> int(value2)
                        del instructions[wire]
                    else:
                        debug_print("unknown operation: "+operation)
                        exit(1)

                elif value1.isdigit() and value2 in wires.keys():
                    debug_print(operation+" operation from other wire: "+value1+" "+operation+" "+value2+"("+str(wires[value2])+") to "+wire)
                    if operation == "AND":
                        wires[wire] = int(value1) & int(wires[value2])
                        del instructions[wire]
                    elif operation == "OR":
                        wires[wire] = int(value1) | int(wires[value2])
                        del instructions[wire]
                    elif operation == "LSHIFT":
                        wires[wire] = int(value1) << int(wires[value2])
                        del instructions[wire]
                    elif operation == "RSHIFT":
                        wires[wire] = int(value1) >> int(wires[value2])
                        del instructions[wire]
                    else:
                        debug_print("unknown operation: "+operation)
                        exit(1)

                elif value1 in wires.keys() and value2.isdigit():
                    debug_print(operation+" operation from other wire: "+value1+"("+str(wires[value1])+") "+operation+" "+value2+" to "+wire)
                    if operation == "AND":
                        wires[wire] = int(wires[value1]) & int(value2)
                        del instructions[wire]
                    elif operation == "OR":
                        wires[wire] = int(wires[value1]) | int(value2)
                        del instructions[wire]
                    elif operation == "LSHIFT":
                        wires[wire] = int(wires[value1]) << int(value2)
                        del instructions[wire]
                    elif operation == "RSHIFT":
                        wires[wire] = int(wires[value1]) >> int(value2)
                        del instructions[wire]
                    else:
                        debug_print("unknown operation: "+operation)
                        exit(1)
                    
                elif value1 in wires.keys() and value2 in wires.keys():
                    debug_print(operation+" operation from other wires: "+value1+"("+str(wires[value1])+") "+operation+" "+value2+"("+str(wires[value2])+") to "+wire)
                    if operation == "AND":
                        wires[wire] = int(wires[value1]) & int(wires[value2])
                        del instructions[wire]
                    elif operation == "OR":
                        wires[wire] = int(wires[value1]) | int(wires[value2])
                        del instructions[wire]
                    elif operation == "LSHIFT":
                        wires[wire] = int(wires[value1]) << int(wires[value2])
                        del instructions[wire]
                    elif operation == "RSHIFT":
                        wires[wire] = int(wires[value1]) >> int(wires[value2])
                        del instructions[wire]
                    else:
                        debug_print("unknown operation: "+operation)
                        exit(1)

                elif value1 not in wires.keys() or value2 in wires.keys():
                    # debug_print(operation+" operation from other wires: "+value1+str(instructions[value1])+" "+operation+" "+value2+"("+wires[value2]+") to "+wire)
                    pass

    print("part2:",wires['a'])


if __name__ == '__main__':
    main()