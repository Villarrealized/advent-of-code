max_calories: int = 0
food: list[int] = []


def process_input(file_name) -> list[str]:
    file = open(file_name, "r", encoding="utf-8")
    return [line.replace("\n", "") for line in file.readlines()]


data: list[str] = process_input("input.txt")

for item in data:
    # Reached end of food list for elf
    if item == "":
        total = sum(food)
        if total > max_calories:
            max_calories = total

        # Reset food list
        food = []
    else:
        food.append(int(item))

print(f"Puzzle 1: {max_calories}")

# Puzzle 2
food = []
elf_food: list[int] = []

for item in data:
    if item == "":
        total = sum(elf_food)
        food.append(total)

        elf_food = []
    else:
        elf_food.append(int(item))

food.sort(reverse=True)
top_three = sum(food[:3])
print(f"Puzzle 2: {top_three}")
