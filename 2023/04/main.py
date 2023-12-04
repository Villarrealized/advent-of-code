from collections import defaultdict

# part 1
def calculate_points(matches):
    if matches == 0: return 0
    return 2 ** (matches - 1)

sum = 0
for line in open("input.txt"):
    line = line.split(':')[1].strip()
    winning_hand, hand = line.split('|')

    winning_hand = winning_hand.split()
    hand = hand.split()

    matches = 0

    for number in hand:
        if number in winning_hand:
            matches += 1

    sum += calculate_points(matches)

print(sum)

# part 2
sum = 0
# Each card starts with 1 copy
cards = defaultdict(lambda: 1)

file = open("input.txt")
lines = file.read().splitlines()

for index, line in enumerate(lines):
    line = line.split(':')[1].strip()
    winning_hand, hand = line.split('|')

    winning_hand = winning_hand.split()
    hand = hand.split()

    matches = 0
    for number in hand:
        if number in winning_hand:
            matches += 1

    copies = cards[index]
    for _ in range(0, copies):
        for i in range(index + 1, index + 1 + matches):
            cards[i] += 1

    sum += cards[index]

print(sum)
