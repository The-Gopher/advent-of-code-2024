from pathlib import Path
from enum import Enum


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
        return (next_x, next_y, dir)

    next_spot: str = map[y + dy][x + dx]

    if next_spot == "#":
        # turn right
        dir = (dir + 1) % 4
        dx, dy = DIRECTIONS[dir].x, DIRECTIONS[dir].y
        return x, y, dir

    return x + dx, y + dy, dir


def in_map(map: list[str], x: int, y: int) -> bool:
    return 0 <= y < len(map) and 0 <= x < len(map[y])


def loops_back(map: list[str], start: tuple[int, int], start_dir: int) -> bool:
    path = [start]
    x, y = start
    dir = (start_dir + 1) % 4

    loop = [(dir, x, y)]
    while in_map(map, x, y):
        x, y, dir = step(map, x, y, dir)
        if (dir, x, y) in loop or ((x, y) == start and dir == start_dir):
            return True
        loop.append((dir, x, y))
        path.append((x, y))
    return False


def copy_map_with_new_object(map: list[str], new_x: int, new_y: int) -> list[str]:
    def process_line(line: str, y: int) -> str:
        if y != new_y:
            return line
        return line[:new_x] + "#" + line[new_x + 1 :]

    ret = [process_line(line, y) for y, line in enumerate(map)]

    return ret


def main():
    input_file = Path(__file__).parent / "input"
    # input_file = Path(__file__).parent / "example"

    map = input_file.read_text().splitlines()

    start_x, start_y, start_dir = find_start(map)
    start_dir = DIRECTIONS.index(Direction.UP)

    # assert loops_back(map, (4, 6), DIRECTIONS.index(Direction.LEFT))
    # assert loops_back(map, (88, 21), 0)
    path = [(start_x, start_y)]
    x, y, dir = start_x, start_y, start_dir

    loops = []
    while in_map(map, x, y):
        x, y, dir = step(map, x, y, dir)
        dx, dy = DIRECTIONS[dir].x, DIRECTIONS[dir].y
        next_x, next_y = x + dx, y + dy
        if (next_x, next_y) not in path and in_map(map, next_x, next_y):
            if loops_back(copy_map_with_new_object(map, next_x, next_y), (x, y), dir):
                loops.append((next_x, next_y))

        path.append((x, y))

    print(len({(x, y) for x, y in path if in_map(map, x, y)}))
    print(len(set(loops)))


if __name__ == "__main__":
    main()
