# part 1
schematic = []
for line in open("input.txt"):
    line = line.strip()
    numbers = ""
    grid = []
    last_index = None

    for index, char in enumerate(line):
        if char.isdigit():
            numbers += char
            last_index = index
        else:
            if numbers.isdigit():
              grid.append({"part": numbers, "index": last_index})
              numbers = ""

            if char != ".":
                grid.append({"part": char, "index": index})

    if numbers.isdigit():
      grid.append({"part": numbers, "index": last_index})
    schematic.append(grid)


def check_neighbors(line, symbol):
    i = symbol["index"]
    sum = 0
    for item in line:
        if item["part"].isdigit():
            num = item["part"]
            if i in range(item["index"] - len(num), item["index"] + 2):
              sum += int(num)

    return sum


sum = 0
for index, line in enumerate(schematic):
    for match in line:
        if not match["part"].isdigit():
            # This symbol may have neighbors on this line
            total = check_neighbors(line, match)
            sum += total
            # Check for neighbors on previous and next lines
            if index > 0:
                prev_line = schematic[index - 1]
                total = check_neighbors(prev_line, match)
                sum += total

            if index < len(schematic) - 1:
                next_line = schematic[index + 1]
                total = check_neighbors(next_line, match)
                sum += total

print(sum)

# part 2
def check_gears(line, symbol):
    i = symbol["index"]
    matches = []
    for item in line:
      if item["part"].isdigit():
          num = item["part"]
          if i in range(item["index"] - len(num), item["index"] + 2):
            matches.append(int(num))

    if len(matches) == 2:
        return matches[0] * matches[1]

    return 0


sum = 0
for index, line in enumerate(schematic):
    for match in line:
        if not match["part"].isdigit():
            # Check gears
            prev_line = []
            next_line = []
            if index > 0:
                prev_line = schematic[index - 1]
            if index < len(schematic) - 1:
                next_line = schematic[index + 1]

            total = check_gears(line + prev_line + next_line, match)
            sum += total
print(sum)
