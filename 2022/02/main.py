# This is an improved version, not how I originally solved it.
# Could make it smaller by getting rid of the constants, but
# I like them because they make it clear what's the win, draw, lose
# condition as opposed to raw numbers

ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
DRAW = 3
LOSE = 0

def puzzle(part_two=False):
  total = 0
  # Opponent choice : instruction : points
  score_card = {
    'A': { 'X': DRAW + ROCK, 'Y': WIN + PAPER, 'Z': LOSE + SCISSORS },
    'B': { 'X': LOSE + ROCK, 'Y': DRAW + PAPER, 'Z': WIN + SCISSORS },
    'C': { 'X': WIN + ROCK, 'Y': LOSE + PAPER, 'Z': DRAW + SCISSORS }
  } if not part_two else  {
    'A': { 'X': LOSE + SCISSORS, 'Y': DRAW + ROCK, 'Z': WIN + PAPER },
    'B': { 'X': LOSE + ROCK, 'Y': DRAW + PAPER, 'Z': WIN + SCISSORS },
    'C': { 'X': LOSE + PAPER, 'Y': DRAW + SCISSORS, 'Z': WIN + ROCK }
  }

  for line in open("input.txt"):
    opponent, instruction = line.split()
    total += score_card.get(opponent).get(instruction)

  print(f"{'Part 1' if not part_two else 'Part 2'}: {total}")


puzzle()
puzzle(part_two=True)