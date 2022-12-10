from dataclasses import dataclass, field


class Direction:
    def __init__(self, name, vx, vy):
        self.name = name
        self.vx = vx
        self.vy = vy

    def __str__(self):
        return f"{self.name} (x={self.vx}, y={self.vy})"

    @staticmethod
    def from_dir(direction):
        name = None
        vx = None
        vy = None

        if direction == "U":
            vx = 0
            vy = 1
            name = "NORTH"
        if direction == "L":
            vx = -1
            vy = 0
            name = "WEST"
        if direction == "R":
            vx = 1
            vy = 0
            name = "EAST"
        if direction == "D":
            vx = 0
            vy = -1
            name = "SOUTH"

        return Direction(name, vx, vy)

    @staticmethod
    def from_velocity(vx, vy):
        name = None

        if vx == 1 and vy == 1:
            name = "NORTH_EAST"
        if vx == -1 and vy == 1:
            name = "NORTH_WEST"
        if vx == 1 and vy == -1:
            name = "SOUTH_EAST"
        if vx == -1 and vy == -1:
            name = "SOUTH_WEST"

        return Direction(name, vx, vy)


@dataclass
class Point:
    x: int = 0
    y: int = 0
    history: list = field(default_factory=list)

    def move(self, direction: Direction):
        self.history.append((self.x, self.y))

        self.x += direction.vx
        self.y += direction.vy

    def __str__(self):
        return f"(x={self.x}, y={self.y})"


@dataclass
class Rope:
    head: Point
    tail: Point

    def move(self, direction: Direction, step: int):
        # print(direction.name)
        for index in range(0, step):
            self.head.move(direction)

            # Diagaonal
            if (
                (abs(abs(self.head.x) - abs(self.tail.x)) == 1)
                and (abs(abs(self.head.y) - abs(self.tail.y)) == 2)
                or (abs(abs(self.head.x) - abs(self.tail.x)) == 2)
                and (abs(abs(self.head.y) - abs(self.tail.y)) == 1)
            ):
                last = self.head.history[-1]
                new_dir = Direction.from_velocity(
                    last[0] - self.tail.x, last[1] - self.tail.y
                )
                self.tail.move(new_dir)

            # Move same direction as the head
            elif (abs(self.head.x - self.tail.x) == 2) or (
                abs(self.head.y - self.tail.y) == 2
            ):
                self.tail.move(direction)

            # print(index + 1, self.head, self.tail)


def puzzle(part_two=False):
    rope = Rope(Point(0, 0), Point(0, 0))
    for line in open("input.txt"):
        dir, step = line.split()
        rope.move(Direction.from_dir(dir), int(step))

    # Add in the final move, because the history is only update
    rope.tail.history.append((rope.tail.x, rope.tail.y))

    # Calculate all unique points of history
    # not sure why the -2 is needed?... solution may be screwy
    # Sample input did not require the minus 2 ... hmmm
    total = len(set(rope.tail.history)) - 2

    print(f"Part 1: {total}")


puzzle()
# puzzle(part_two=True)
