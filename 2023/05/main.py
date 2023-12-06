seeds = []
maps = []

map = []
for index, line in enumerate(open("input.txt")):
    if index == 0:
        name, values = line.split(":")
        seeds = [int(value) for value in values.strip().split()]
    else:
        if line[0].isalpha():
            if len(map):
                maps.append(map)
            map = []
        elif line[0].isdigit():
            map.append([int(value) for value in line.strip().split()])

# Add the last map
maps.append(map)

locations = []
for seed in seeds:
    val = seed
    for map in maps:
        for row in map:
            dest, source, count = row
            offset = dest - source
            # print(offset)
            if val in range(source, source + count):
                val += offset
                break

    locations.append(val)

print(min(locations))


# part 2
seeds = []
maps = []

map = []
for index, line in enumerate(open("input.txt")):
    if index == 0:
        name, values = line.split(":")
        instructions = [int(value) for value in values.strip().split()]
        for i in range(0, len(instructions), 2):
            val = instructions[i]
            count = instructions[i + 1]
            seeds.extend(list(range(val, val + count)))
    else:
        if line[0].isalpha():
            if len(map):
                maps.append(map)
            map = []
        elif line[0].isdigit():
            map.append([int(value) for value in line.strip().split()])

# Add the last map
maps.append(map)

locations = []
for index, seed in enumerate(seeds):
    if index in [0, 1_000_000, 10_000_000, 100_000_000, 1_000_000_000, 2_000_000_000]:
        print(f"Processing seed {index + 1} of {len(seeds)}")
    val = seed
    for map in maps:
        for row in map:
            dest, source, count = row
            offset = dest - source
            if val in range(source, source + count):
                val += offset
                break

    locations.append(val)

print(min(locations))
