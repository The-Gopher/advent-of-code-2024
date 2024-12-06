from pathlib import Path

DIRECTIONS = [
    (1, 0),
    (0, -1),
    (-1, 0),
    (0, 1),
]


def find_start(map: list[str]) -> tuple[int, int, str]:
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char not in (".", "#"):
                return x, y, char
    raise ValueError("No start found")


def step(map: list[str], x: int, y: int, dir: int) -> tuple[int, int, int]:
    dx, dy = DIRECTIONS[dir]
    next_x, next_y = x + dx, y + dy
    if not in_map(map, next_x, next_y):
        return (-1, -1, 1)
    
    next_spot: str = map[y + dy][x + dx]

    if next_spot == "#":
        # turn right
        dir = (dir - 1) % 4
        dx, dy = DIRECTIONS[dir]
        return x + dx, y + dy, dir

    return x + dx, y + dy, dir


def in_map(map: list[str], x: int, y: int) -> bool:
    return 0 <= y < len(map) and 0 <= x < len(map[y])


def main():
    input_file = Path(__file__).parent / "input"
    map = input_file.read_text().splitlines()

    start_x, start_y, start_dir = find_start(map)
    # assert start_dir == "^"
    start_dir = DIRECTIONS.index((0, -1))

    # assert step(map, 4, 1, 1) == (5, 1, 0), step(map, 4, 1, 1)

    path = [(start_x, start_y)]
    x, y, dir = start_x, start_y, start_dir
    while in_map(map, x, y):
        x, y, dir = step(map, x, y, dir)
        path.append((x, y))
    print(len({(x, y) for x, y in path if in_map(map, x, y)}))


def answer_to_points():
    answer = """....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X.."""
    points = []
    for y, line in enumerate(answer.splitlines()):
        for x, char in enumerate(line):
            if char == "X":
                points.append((x, y))
    print(list(sorted(points)))


if __name__ == "__main__":
    main()
