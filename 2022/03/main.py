import string

priorities = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1,53)))

def puzzle_one():
  total = 0
  for line in open("input.txt"):
    rucksack = line.strip()

    half_length: int = len(rucksack) // 2
    # Get the unique values from each compartment to compare
    compartment_1 = ''.join(set(rucksack[:half_length]))
    compartment_2 = ''.join(set(rucksack[half_length:]))

    for item in compartment_1:
      index = compartment_2.find(item)
      if index != -1:
        total += priorities[item]

  print(f"Part 1: {total}")

puzzle_one()

def puzzle_two():
  total = 0
  group = []
  for line in open("input.txt"):
    rucksack = line.strip()
    # Add each rucksack to a group as a set
    group.append(set(rucksack))
    if len(group) == 3:
      # Find the intersection of all three rucksacks
      badge_item = list(group[0].intersection(group[1], group[2]))[0]
      total += priorities[badge_item]
      group = []

  print(f"Part 2: {total}")

puzzle_two()