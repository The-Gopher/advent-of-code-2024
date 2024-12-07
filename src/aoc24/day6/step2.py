from pathlib import Path
from enum import Enum
from itertools import product
from turtle import up
from xmlrpc.client import Boolean


class Direction(Enum):
    UP = (0, -1)
    LEFT = (-1, 0)
    DOWN = (0, 1)
    RIGHT = (1, 0)

    @property
    def x(self) -> int:
        return self.value[0]

    @property
    def y(self) -> int:
        return self.value[1]


DIRECTIONS = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]


def find_start(map: list[str]) -> tuple[int, int, str]:
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char not in (".", "#"):
                return x, y, char
    raise ValueError("No start found")


def find_objects(map: list[str]) -> list[tuple[Direction, tuple[int, int]]]:
    objects = []

    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char not in (".", "^", "v", "<", ">"):
                for dir in DIRECTIONS:
                    # Step back 1
                    x2, y2 = x - dir.x, y - dir.y
                    if in_map(map, x2, y2):
                        objects.append((dir, (x2, y2)))
    return objects


def path_out(map: list[str], start: tuple[int, int], dir: int) -> list[tuple[int, int]]:
    path = [start]
    x, y = start
    while in_map(map, x, y):
        x, y, dir = step(map, x, y, dir)
        path.append((x, y))
    return path


def step(map: list[str], x: int, y: int, dir: int) -> tuple[int, int, int]:
    dx, dy = DIRECTIONS[dir].x, DIRECTIONS[dir].y
    next_x, next_y = x + dx, y + dy
    if not in_map(map, next_x, next_y):
        return (-1, -1, 1)

    next_spot: str = map[y + dy][x + dx]

    if next_spot == "#":
        # turn right
        dir = (dir + 1) % 4
        dx, dy = DIRECTIONS[dir].x, DIRECTIONS[dir].y
        return x + dx, y + dy, dir

    return x + dx, y + dy, dir


def in_map(map: list[str], x: int, y: int) -> bool:
    return 0 <= y < len(map) and 0 <= x < len(map[y])


def loops_back(map: list[str], start: tuple[int, int], start_dir: int) -> bool:
    path = [start]
    x, y = start
    dir = (start_dir + 1) % 4
    while in_map(map, x, y):
        x, y, dir = step(map, x, y, dir)
        if (x, y) == start and dir == start_dir:
            print(path)
            return True
        path.append((x, y))
    return False


def main():
    input_file = Path(__file__).parent / "input"
    input_file = Path(__file__).parent / "example"

    map = input_file.read_text().splitlines()

    start_x, start_y, start_dir = find_start(map)
    # assert start_dir == "^"
    start_dir = DIRECTIONS.index(Direction.UP)

    # assert loops_back(map, (4, 6), DIRECTIONS.index(Direction.LEFT))
    path = [(start_dir, start_x, start_y)]
    x, y, dir = start_x, start_y, start_dir

    loops = []
    while in_map(map, x, y):
        x, y, dir = step(map, x, y, dir)

        if loops_back(map, (x, y), dir):
            print("Loop back")
            break

        path.append((dir, x, y))

    object_adjacents = find_objects(map)
    ups = [space for dir, space in object_adjacents if dir == Direction.UP] + [None]
    rights = [space for dir, space in object_adjacents if dir == Direction.RIGHT] + [
        None
    ]
    downs = [space for dir, space in object_adjacents if dir == Direction.DOWN] + [None]
    lefts = [space for dir, space in object_adjacents if dir == Direction.LEFT] + [None]

    for a, b, c, d in product(ups, rights, downs, lefts):
        if (a, b, c, d).count(None) != 1:
            continue
        # Up to Right
        if a is not None and b is not None and (a[0] >= b[0] or a[1] != b[1]):
            continue
        # Right to Down
        if b is not None and c is not None and (b[0] != c[0] or b[1] >= c[1]):
            continue
        # Down to Left
        if c is not None and d is not None and (c[0] <= d[0] or c[1] != d[1]):
            continue
        # Left to Up
        if d is not None and a is not None and (d[0] != a[0] or d[1] <= a[1]):
            continue
        print(a, b, c, d)

    # assert step(map, 4, 1, 1) == (5, 1, 0), step(map, 4, 1, 1)

    path = [(start_x, start_y)]
    x, y, dir = start_x, start_y, start_dir
    while in_map(map, x, y):
        x, y, dir = step(map, x, y, dir)
        path.append((x, y))
    print(len({(x, y) for x, y in path if in_map(map, x, y)}))


if __name__ == "__main__":
    main()
