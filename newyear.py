import argparse, os, shutil as sh
from datetime import date

DEBUG = False
FORCE = False

def parse_input(input_data):
    # DEFINE CUSTOM PARSING HERE
    ...


def debug_print(msg):
    # Use ANSI escape codes to set the text color to yellow
    global DEBUG
    if DEBUG:
        print('\033[33m[+]\033[0m', msg)

def error_print(msg):
    # Use ANSI escape codes to set the text color to red
    print('\033[31m-\033[0m', msg)

def main():
    global DEBUG, FORCE
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process some input.')
    parser.add_argument('--debug', action='store_true', help='enable debug messages')
    parser.add_argument('--force', action='store_true', help='this overwrites any dayXX.py files if already present')
    parser.add_argument('year', nargs="*", help='the year(s) to create the folder for')
    
    # Parse command-line arguments
    args = parser.parse_args()
    
    # Print debug messages if --debug flag is set
    if args.debug:
        DEBUG = True
        debug_print('Debug mode enabled')

    # Overwrite files if --force flag is set
    if args.force:
        FORCE = True
        debug_print('Forcing overwrites')

    # Use year if passed, otherwise create for this year
    if args.year:
        year = args.year
    else:
        year = [str(date.today().year)]

    # Check for year directory, exit if found (if not forcing)
    for y in year:
        if os.path.exists(y) and not FORCE:
            error_print(y+" year directory already exists - exiting.")
            exit()
        elif os.path.exists(y) and FORCE:
            debug_print(y+" directory exists - re-initializing.")
            # Pass here for creating directory.
        else:
            debug_print("Creating "+y+" directory.")
            os.mkdir(y)

        # Make subdirs and copy template to each one.
        for day in range(1,26):
            dir = y + "/day "+str(day).rjust(2,"0")+"/python/"
            file = "day"+str(day).rjust(2,"0")+".py"
            if os.path.exists(dir):
                debug_print(dir+" exists, just overwriting file")
            else:
                debug_print("Creating "+dir+" directory.")
                os.makedirs(dir)

            debug_print("Copying template.py to "+file+" in "+dir+".")
            sh.copy("template.py",dir+file)
        
    


if __name__ == '__main__':
    main()