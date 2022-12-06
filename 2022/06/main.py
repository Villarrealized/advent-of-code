def puzzle(part_two=False):
  stream = []
  for line in open("input.txt"):
    for index, char in enumerate(line):
      if char in stream:
        item_index = stream.index(char)
        # clip the start of the list off until we remove the duplicate character
        stream = stream[item_index + 1:]

      # Always add the new char
      stream.append(char)

      marker_length = 14 if part_two else 4
      if len(stream) == marker_length:
        print(f"{'Part 1' if not part_two else 'Part 2'}: {index + 1}")
        break

puzzle()
puzzle(part_two=True)