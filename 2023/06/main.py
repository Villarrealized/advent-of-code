from functools import reduce
# part 1
file = open("input.txt")
lines = file.read().splitlines()
_, times = lines[0].split(':')
_, distances = lines[1].split(':')
times = [int(t) for t in times.split()]
distances = [int(d) for d in distances.split()]

outcomes = [[],[],[],[]]
for i in range(0, len(times)):
  race_length = times[i]
  record = distances[i]

  for power in range (1, race_length):
    time = race_length - power
    distance = power * time
    if distance > record:
      outcomes[i].append(distance)

product = reduce(lambda count, l: count * len(l), outcomes, 1)
print(product)


# part 2
file = open("input.txt")
lines = file.read().splitlines()
_, times = lines[0].split(':')
_, distances = lines[1].split(':')
race_length = int(times.replace(' ', ''))
record = int(distances.replace(' ', ''))

outcomes = []

for power in range (1, race_length):
    time = race_length - power
    distance = power * time
    if distance > record:
        outcomes.append(distance)

print(len(outcomes))





