def puzzle_one():
  total = 0
  for line in open("input.txt"):
    pairs = line.strip().split(',')
    x1, x2 = [int(id) for id in pairs[0].split('-')]
    y1, y2 = [int(id) for id in pairs[1].split('-')]

    # Test if either pair of numbers contains the other
    if (x1 >= y1 and x2 <= y2) or (y1 >= x1 and y2 <= x2):
      total +=1

  print(f"Part 1: {total}")

puzzle_one()

def puzzle_two():
  total = 0
  for line in open("input.txt"):
    pairs = line.strip().split(',')
    x1, x2 = [int(id) for id in pairs[0].split('-')]
    y1, y2 = [int(id) for id in pairs[1].split('-')]

    # Intersection
    if x1 <= y2 and y1 <= x2:
      total += 1

  print(f"Part 2: {total}")

puzzle_two()