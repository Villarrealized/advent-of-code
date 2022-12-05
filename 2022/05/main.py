def parse_crates(data: list[str]) -> list[list[str]]:
  crates:list[list[str]] = []

  for line in data:
    # We don't need to parse the input after we get to the numbers
    if line[1] == '1':
      break

    # The maximum number of stacks this line width contains (0-indexed)
    max_stacks = (len(line) // 4)
    for stack in range(0, max_stacks):
      # Formula to find the position of the crate letter
      index = (stack * 4) + 1
      crate = line[index]

      # If stack does not exist, create it
      if stack >= len(crates):
        crates.append([])

      # Add crate to the right stack if its not empty
      if crate.isalpha():
        crates[stack].append(crate)

  return crates


def parse_instructions(data: list[str]) -> list[list[int]]:
  '''
  Crate moving instructions decoder:
  1st number = quantity
  2nd number = from stack
  3rd number = to stack
  '''
  instructions = []

  for line in data:
    if (line.startswith('move')):
      instructions.append([int(char) for char in line.split() if char.isnumeric()])

  return instructions


def puzzle(part_two = False):
  file = open("input.txt")
  data = file.readlines()

  crates = parse_crates(data)
  instructions = parse_instructions(data)

  # Move all crates according to instructions
  for instruction in instructions:
    qty, stack_from, stack_to = instruction
    # Need to subtract one to get correct list index
    stack_from = stack_from - 1
    stack_to = stack_to - 1

    # Get the crates to move
    crate = crates[stack_from][:qty]
    # Copy the crates to the top of the stack, one at a time
    # This results in a reversed order
    if not part_two:
      crates[stack_to][:0] = reversed(crate)
    else:
      # The CraneMover 9001 can move a stack all at once. No need
      # for one by one movement
      crates[stack_to][:0] = crate
    # Delete the copied crates from the original stack
    # to complete the "move" instruction
    del crates[stack_from][:qty]

  # Get crate letters at top of each stack
  stack_top_code = ''.join([stack[0] for stack in crates])

  print(f"{'Part 1' if not part_two else 'Part 2'}: {stack_top_code}")

puzzle()
puzzle(part_two=True)