import re
# # part 1
pairs = []

for line in open("input.txt"):
  numbers = []
  for char in line:
    if char.isdigit():
      numbers.append(char)

  pairs.append(int(f"{numbers[0]}{numbers[-1]}"))

print(sum(pairs))


# part 2
number_map = {
  "zero": "0",
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9"
}

parsed = []

for line in open("input.txt"):
  line = line.replace("\n", "")
  pairs = []
  for key, value in number_map.items():
    number_indices = [m.start() for m in re.finditer(value, line)]
    word_indices = [m.start() for m in re.finditer(key, line)]

    if len(number_indices) > 0:
      for index in number_indices:
        pairs.append((value, index))
    if len(word_indices) > 0:
      for index in word_indices:
        pairs.append((value, index))

  parsed.append(pairs)


pairs = []
for line in parsed:
  line = sorted(line, key=lambda x: x[1])
  pairs.append(int(f"{line[0][0]}{line[-1][0]}"))

print(sum(pairs))