# seeds = []
# _maps = []

# _map = []
# for index, line in enumerate(open("input.txt")):
#     if index == 0:
#         name, values = line.split(":")
#         seeds = [int(value) for value in values.strip().split()]
#     else:
#         if line[0].isalpha():
#             if len(_map):
#                 _maps.append(_map)
#             _map = []
#         elif line[0].isdigit():
#             _map.append([int(value) for value in line.strip().split()])

# # Add the last _map
# _maps.append(_map)

# locations = []
# for seed in seeds:
#     val = seed
#     for _map in _maps:
#         for row in _map:
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
_maps = []
_map = []
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
            if len(_map):
                _maps.append(_map)
            _map = []
        elif line[0].isdigit():
            _map.append([int(value) for value in line.strip().split()])

# Add the last _map
_maps.append(_map)


def process(seed):
    val = seed
    count = 1
    for _map in _maps:
        for row in _map:
            dest, source, count = row
            offset = dest - source
            if val in range(source, source + count):
                val += offset
                count += 1
                break

    yield val

import sys
if __name__ == "__main__":
    length = len(seeds)
    print(f"begin processing {length} seeds")
    # pool = Pool()
    # for value in tqdm.tqdm(pool.imap_unordered(process, seeds, chunksize=4), total=length):
    min = sys.maxsize
    for ready in tqdm.tqdm(map(process, seeds), total=length):
        for value in ready:
            if value < min:
                min = value
                print(f"new min: {min}")

    print(min)


