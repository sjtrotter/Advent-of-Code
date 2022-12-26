def move_elves(grid, elves):
  # Initialize variables to store the proposed moves for each Elf and the bounds of the rectangle
  proposed_moves = {}
  min_row, max_row, min_col, max_col = float('inf'), -float('inf'), float('inf'), -float('inf')
  
  # Iterate over the positions of the Elves
  for i, j in elves:
    # Update the bounds of the rectangle
    min_row = min(min_row, i)
    max_row = max(max_row, i)
    min_col = min(min_col, j)
    max_col = max(max_col, j)
    
    # Initialize a variable to store the proposed move for the current Elf
    proposed_move = (i, j)
    
    # Check if there is an Elf in the N, NE, or NW positions
    if (i-1, j) in elves or (i-1, j+1) in elves or (i, j+1) in elves:
      # If there is no Elf in the S, SE, or SW positions, propose moving south
      if (i+1, j) not in elves and (i+1, j-1) not in elves and (i, j-1) not in elves:
        proposed_move = (i+1, j)
    # Check if there is an Elf in the S, SE, or SW positions
    elif (i+1, j) in elves or (i+1, j-1) in elves or (i, j-1) in elves:
      # If there is no Elf in the N, NE, or NW positions, propose
      # If there is no Elf in the N, NE, or NW positions, propose moving north
      if (i-1, j) not in elves and (i-1, j+1) not in elves and (i, j+1) not in elves:
        proposed_move = (i-1, j)
      # If there is no Elf in the W, NW, or SW positions, propose moving west
      elif (i, j-1) not in elves and (i-1, j-1) not in elves and (i-1, j) not in elves:
        proposed_move = (i, j-1)
      # If there is no Elf in the E, NE, or SE positions, propose moving east
      elif (i, j+1) not in elves and (i-1, j+1) not in elves and (i-1, j) not in elves:
        proposed_move = (i, j+1)
    
    # Store the proposed move for the current Elf
    proposed_moves[(i, j)] = proposed_move
  
  # Initialize a variable to store the count of empty spaces
  empty_spaces = 0
  
  # Iterate over the proposed moves
  for i, j in proposed_moves.values():
    # Check if the current position is outside the bounds of the rectangle
    if i < min_row or i > max_row or j < min_col or j > max_col:
      # Update the bounds of the rectangle
      min_row = min(min_row, i)
      max_row = max(max_row, i)
      min_col = min(min_col, j)
      max_col = max(max_col, j)
    
    # Check if the current position is empty
    if grid[i][j] == '.':
      empty_spaces += 1
  
  # Return the count of empty spaces
  return empty_spaces

# Example usage
grid = [
  '....#..',
  '..###.#',
  '#...#.#',
  '.#...##',
  '#.###..',
  '##.#.##',
  '.#..#..'
]
elves = [(0, 4), (1, 5), (1, 6), (2, 1), (2, 3), (3, 2), (3, 4), (4, 1), (4, 5), (5, 1), (5, 4), (6, 1)]
print(move_elves(grid, elves))