# seeds = []
# maps = []

# map = []
# for index, line in enumerate(open("input.txt")):
#     if index == 0:
#         name, values = line.split(":")
#         seeds = [int(value) for value in values.strip().split()]
#     else:
#         if line[0].isalpha():
#             if len(map):
#                 maps.append(map)
#             map = []
#         elif line[0].isdigit():
#             map.append([int(value) for value in line.strip().split()])

# # Add the last map
# maps.append(map)

# locations = []
# for seed in seeds:
#     val = seed
#     for map in maps:
#         for row in map:
#             dest, source, count = row
#             offset = dest - source
#             # print(offset)
#             if val in range(source, source + count):
#                 val += offset
#                 break

#     locations.append(val)

# print(min(locations))

from multiprocessing import Pool
import tqdm

# part 2
import tqdm

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


def process(seed):
    val = seed
    count = 1
    for map in maps:
        for row in map:
            dest, source, count = row
            offset = dest - source
            if val in range(source, source + count):
                val += offset
                count += 1
                break

    return val


if __name__ == "__main__":
    length = len(seeds)
    print(f"begin processing {length} seeds")
    pool = Pool()
    values = set(tqdm.tqdm(pool.imap_unordered(process, seeds), total=length))

    print(min(values))
