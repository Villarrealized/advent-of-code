
ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
DRAW = 3
LOSE = 0

def calculate_points(match: list[str]) -> int:
  # Rock
  if match[0] == 'A':
    if match[1] == 'X':
      return DRAW + ROCK
    if match[1] == 'Y':
      return WIN + PAPER
    if match[1] == 'Z':
      return LOSE + SCISSORS

  # Paper
  if match[0] == 'B':
    if match[1] == 'X':
      return LOSE + ROCK
    if match[1] == 'Y':
      return DRAW + PAPER
    if match[1] == 'Z':
      return WIN + SCISSORS

  # Scissors
  if match[0] == 'C':
    if match[1] == 'X':
      return WIN + ROCK
    if match[1] == 'Y':
      return LOSE + PAPER
    if match[1] == 'Z':
      return DRAW + SCISSORS


match_points: list[int] = []

for line in open("input.txt"):
  match_points.append(calculate_points(line.split()))

print(f"Puzzle 1: {sum(match_points)} points")




