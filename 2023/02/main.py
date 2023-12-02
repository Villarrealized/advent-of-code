# part 1
red_cubes = 12
green_cubes = 13
blue_cubes = 14

sum = 0

for index, line in enumerate(open("input.txt")):
  line = line.split(':')[1].strip()
  sets = line.split(';')

  possible = True
  for set in sets:
    cubes = set.split(',')
    for cube in cubes:
      number, color = cube.strip().split()
      number = int(number)
      match color:
        case "red":
          if number > red_cubes:
            possible = False
        case "green":
          if number > green_cubes:
            possible = False
        case "blue":
          if number > blue_cubes:
            possible = False

  if possible:
    sum += index + 1

print(sum)

# part 2
sum = 0
for index, line in enumerate(open("input.txt")):
  line = line.split(':')[1].strip()
  sets = line.split(';')

  min_red = 0
  min_green = 0
  min_blue = 0

  for set in sets:
    cubes = set.split(',')
    for cube in cubes:
      number, color = cube.strip().split()
      number = int(number)
      match color:
        case "red":
          if number > min_red:
            min_red = number
        case "green":
          if number > min_green:
            min_green = number
        case "blue":
          if number > min_blue:
            min_blue = number

  sum += (min_blue * min_green * min_red)

print(sum)