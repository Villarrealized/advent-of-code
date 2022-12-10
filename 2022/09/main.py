from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


# @dataclass
# class Rope:
#     head: Point
#     tail: Point

#     def move(self, to: Point):
#         self.head +=


def puzzle(part_two=False):
    total = 0
    for line in open("input.txt"):
        command = line.split()

    print(f"Part 1: {total}")


puzzle()
# puzzle(part_two=True)
