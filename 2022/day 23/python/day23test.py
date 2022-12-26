import argparse
from elf import *
from grid import *

DEBUG = False

def parse_input(input_data):
    # DEFINE CUSTOM PARSING HERE
    data = [line.strip() for line in input_data.split('\n')]

    # data = input_data.split("\n").strip()

    return data

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

    # create grid from data
    grid = Grid(len(data[0]),len(data),debug=DEBUG)

    # find elves, create them from data
    elfData = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "#":
                elfData.append((x,y))

    elves = []
    for elf in elfData:
        elves.append(Elf(elf[0],elf[1],grid))

    #initialize directions
    directions = ["N","S","W","E"]

    # for 10 rounds (part1)
    # totalrounds = 10
    # for rounds in range(totalrounds):

    # for until moves == 0 (part2)
    stop = False
    rounds = 0
    while not stop:
        rounds += 1
        proposals = []
        # for each elf
        for elf in elves:
            # propose = (elf, elf.propose(directions))
            # uncomment to check the moves:
            # debug_print(str(rounds)+str(elf.propose(directions)))
            proposals.append((elf,elf.propose(directions)))

        moves = 0 # for part 2
        for elf in elves:
            move = True
            for elfcomp in elves:
                if elf != elfcomp and elf.proposal == elfcomp.proposal:
                    move = False
            if move and elf.proposal != elf.position:
                moves += 1 # for part 2
                elf.move(elf.proposal[0],elf.proposal[1])

        if moves == 0:
            stop = True
        else:
            # debug_print("current round: "+str(rounds)+", elves: "+str(len(elves))+", moved: "+str(moves))
            debug_print("current round: "+str(rounds)+", elves moved: "+str(moves))

        # at end of round, rotate directions
        directions.append(directions.pop(0))

    # after rounds, get total blank spaces
    debug_print(str(grid))
    # for part1
    # print("part1:",grid.countBlanks())
    # for part2
    print("part2:",rounds)



if __name__ == '__main__':
    main()