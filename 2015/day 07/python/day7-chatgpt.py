with open("../input.txt", 'r') as f:
    input = f.read()

# Create a dictionary to store the instructions
instructions = {}

# Split the input into a list of lines
lines = input.split("\n")

# Iterate over the lines to store the instructions in the dictionary
for line in lines:
  # Split the line into its parts
  parts = line.split(" ")

  # Get the output wire
  output_wire = parts[-1]

  # Store the instruction in the dictionary
  if parts[1] == "->":
    if parts[0].isdigit():
      instructions[output_wire] = ("ASSIGN", (parts[0],))
    else:
      instructions[output_wire] = ("DIRECT", (parts[0],))
  elif parts[0] == "NOT":
    instructions[output_wire] = ("NOT", (parts[1],))
  else:
    instructions[output_wire] = (parts[1], (parts[0], parts[2]))

# Create a dictionary to store the values of the wires
wires = {}

# Iterate over the instructions to calculate the values of the wires
while instructions:
  for output_wire, instruction in list(instructions.items()):
    operation = instruction[0]
    if operation == "NOT":
      input_wire = instruction[1]
      if input_wire in wires:
        wires[output_wire] = ~wires[input_wire] & 0xffff
        del instructions[output_wire]
    elif operation in ("AND", "OR", "LSHIFT", "RSHIFT"):
      input1 = wires.get(instruction[0][0], instruction[0][0])
      input2 = wires.get(instruction[0][1], instruction[0][1])
      if input1.isdigit() and input2.isdigit():
        if operation == "AND":
          wires[output_wire] = int(input1) & int(input2)
        elif operation == "OR":
          wires[output_wire] = int(input1) | int(input2)
        elif operation == "LSHIFT":
          wires[output_wire] = int(input1) << int(input2)
        elif operation == "RSHIFT":
          wires[output_wire] = int(input1) >> int(input2)
        del instructions[output_wire]
    elif operation == "ASSIGN":
      wires[output_wire] = int(instruction[0][0])
      del instructions[output_wire]
    elif operation == "DIRECT":
      input_wire = instruction[0][0]
      if input_wire in wires:
        wires[output_wire] = wires[input_wire]
        del instructions[output_wire]

# Print the value of the wire "a"
print(wires["a"])