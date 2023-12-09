import math
# directions = 'LR'
directions = 'LLRRRLRLLRRLLRLRLRLRRLRRRLRRRLRLRRLLRLLRRRLRRLRRRLRLRRRLRRLRLRRRLRRRLRRLRLRRRLRRLRRLRRRLRLRLLRLLRLLRLRRRLRRLRRLRRRLRLRRRLRLRLRLRRRLRRRLRLRLRLRRRLRLLRRLLRLLRRLRRRLLRRRLLRRLRLRRLRLLRLLLLRRLLRRLRRLRLLLRRRLRRLRRRLRRLLRLRRRLRLLRRRLLLLRLRRRLRLRRLRRLRRLLRLRLRRLLLRRLLRLRRLRRRR'

network = {}
for line in open("input.txt"):
  key, value = line.strip().split('=')
  left, right = value.replace('(', '').replace(')', '').strip().split(', ')
  network[key.strip()] = [left, right]


# part 1
# steps = 0
# cur_key = 'AAA'
# end = False


# while cur_key != 'ZZZ':
#   for dir in directions:
#     steps += 1

#     values = network[cur_key]
#     index = 0
#     if dir == 'R': index = 1

#     cur_key = values[index]

#     if cur_key == 'ZZZ': break

# print(steps)




# part 2
end = False
keys = [key for key in network.keys() if key[-1] == 'A']

end = False
steps = 0

count = {}

while not end:
  for dir in directions:
    if end: break
    index = 0
    next_keys = []

    if dir == 'R': index = 1

    for i, key in enumerate(keys):
      values = network[key]
      next_keys.append(values[index])
      if values[index][-1] == 'Z':
        count[i] = steps + 1
        if len(count) == len(keys):
          end = True
          break

    keys = next_keys
    steps += 1

print(math.lcm(*count.values()))