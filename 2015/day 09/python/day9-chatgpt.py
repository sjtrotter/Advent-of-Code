#chatgpt couldn't quite figure it out, but i got the start with its suggestions.



import argparse

DEBUG = False

def parse_input(input_data):
    # DEFINE CUSTOM PARSING HERE
    distances = [line.strip() for line in input_data.split('\n')]

    cityDistances = {}
    for line in distances:
        if line == "": break
        parts = line.split(" ")
        if not parts[0] in cityDistances.keys():
            cityDistances[parts[0]] = []
        if not parts[2] in cityDistances.keys():
            cityDistances[parts[2]] = []

        cityDistances[parts[0]].append((parts[2],int(parts[-1])))
        cityDistances[parts[2]].append((parts[0],int(parts[-1])))

    return cityDistances

def debug_print(msg):
    # Use ANSI escape codes to set the text color to yellow
    global DEBUG
    if DEBUG:
        print('\033[33m[+]\033[0m', msg)





##### CHAT GPT FUNCTION
def shortest_route(cityDistances, locations, start_loc=None, visited_cities=None, total_distance=0, path=None):
  # Initialize shortest_distance to a large number
  shortest_distance = float("inf")
  # Initialize the shortest_path to an empty list
  shortest_path = []

  # Initialize variables if not provided
  if start_loc is None:
    start_loc = locations[0]
  if visited_cities is None:
    visited_cities = locations.copy()
  if path is None:
    path = [start_loc]

  # Remove the starting location from the list of visited cities
  visited_cities.remove(start_loc)

  # Base case: If all cities have been visited, return the total distance and path
  if len(path) == len(locations):
    return total_distance + cityDistances[start_loc][path[0]][1], path

  # Recursive case: Try all possible next cities
  for next_city, distance in cityDistances[start_loc]:
    if next_city not in visited_cities:
      # Calculate the distance and path starting from the next city
      distance, path = shortest_route(cityDistances, locations, next_city, visited_cities + [start_loc], total_distance + distance, path + [next_city])
      # Update shortest_distance and shortest_path if necessary
      if distance < shortest_distance:
        shortest_distance = distance
        shortest_path = path
  
  return shortest_distance, shortest_path





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
        debug_print(f'Read input from {args.input_file}: \n{input_data}')


    # CODE REST OF PROBLEM MAINLOOP HERE
    cityDistances = parse_input(input_data) # Customize to problem

    debug_print(cityDistances)

############### CHAT GPT CODE
    # Get the list of locations
    locations = list(cityDistances.keys())

    # Find the shortest route
    shortest_distance, shortest_path = shortest_route(cityDistances, locations)
    print(shortest_distance)
    print(shortest_path)


if __name__ == '__main__':
    main()