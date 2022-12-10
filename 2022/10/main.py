def puzzle(part_two=False):
    cycles = []
    cycle = 0
    x = 1
    for line in open("input.txt"):
        command = line.split()
        if command[0] == "noop":
            cycle += 1
            cycles.append(x)
            continue
        else:
            for _ in range(0, 2):
                cycle += 1
                cycles.append(x)

            x += int(command[1])

    total = 0
    for index in range(19, len(cycles), 40):
        total += (index + 1) * cycles[index]
    # print(signal_strengths)
    # print(sum(signal_strengths))
    print(f"Part 1: {total}")


puzzle()
# puzzle(part_two=True)
