from pathlib import Path
from typing import List, Set, Tuple

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def main():
    file = Path(__file__).parent / "input"
    # file = Path(__file__).parent / "example"

    with file.open("r") as f:
        topo_map: List[List[int]] = [
            [int(x) for x in line] for line in f.read().splitlines()
        ]

    score_map: List[List[None | int]] = [
        [None for _ in range(len(topo_map[0]))] for _ in range(len(topo_map))
    ]

    x_size = len(topo_map[0])
    y_size = len(topo_map)

    for i in range(9, -1, -1):
        for y in range(y_size):
            for x in range(x_size):
                if topo_map[y][x] == i:
                    if i == 9:
                        score_map[y][x] = 1
                    else:
                        cell_value = 0
                        for d in DIRECTIONS:
                            new_y = y + d[0]
                            new_x = x + d[1]
                            if (
                                0 <= new_y < y_size
                                and 0 <= new_x < x_size
                                and topo_map[new_y][new_x] == i + 1
                            ):
                                cell_value += score_map[new_y][new_x] or 0
                        score_map[y][x] = cell_value

    score = 0
    for y in range(y_size):
        for x in range(x_size):
            if topo_map[y][x] == 0:
                score += score_map[y][x]
    print(score)


if __name__ == "__main__":
    main()
