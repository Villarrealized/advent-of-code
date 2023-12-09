
sequences = {}
for index, line in enumerate(open("input.txt")):
  seq = [int(n) for n in line.strip().split()]
  sequences[index] = [seq]

# Calculate diff and add new sequences
for i, sequence in sequences.items():
  sequence = sequence[0]
  while True:
    new = [r-l for l, r in zip(sequence[:-1], sequence[1:])]
    sequences[i].append(new)
    if (len(list(set(new))) == 1 and new[0] == 0):
      break

    sequence = new

def part1():
  for sequence in sequences.values():
    index = -1
    while abs(index) <= len(sequence):
      if index == -1:
        sequence[index].append(0)
      elif index == -2:
        sequence[index].append(sequence[index][-1])
      else:
        sequence[index].append(sequence[index][-1] + sequence[index + 1][-1])

      index -= 1

  sum = 0
  for sequence in sequences.values():
    sum += sequence[0][-1]

  print(sum)

# part1()
def part2():
  for sequence in sequences.values():
    length = len(sequence) - 1
    index = length
    while index >= 0:
      if index == length:
        sequence[index].insert(0, 0)
      elif index == length - 1:
        sequence[index].insert(0, sequence[index][0])
      else:
        sequence[index].insert(0,  sequence[index][0] - sequence[index + 1][0])
        print(sequence[index])

      index -= 1

  sum = 0
  for sequence in sequences.values():
    sum += sequence[0][0]

  print(sum)

part2()