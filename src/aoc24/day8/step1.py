from itertools import combinations, groupby, pairwise
from pathlib import Path
from enum import Enum


def find_antennas(map: list[str]) -> dict[str, list[tuple[int, int]]]:
    antennas = []
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char != ".":
                antennas.append((char, x, y))
    return {
        f: [(x, y) for f, x, y in v]
        for f, v in groupby(sorted(antennas), key=lambda x: x[0])
    }


def find_antinodes(a: tuple[int, int], b: tuple[int, int]) -> list[tuple[int, int]]:
    x1, y1 = a
    x2, y2 = b

    x3 = 2 * x1 - x2
    y3 = 2 * y1 - y2

    x4 = 2 * x2 - x1
    y4 = 2 * y2 - y1

    return [(x3, y3), (x4, y4)]


def in_map(map: list[str], point: tuple[int, int]) -> bool:
    x, y = point
    return 0 <= x < len(map[0]) and 0 <= y < len(map)


def main():
    input_file = Path(__file__).parent / "input"
    # input_file = Path(__file__).parent / "example"

    map = input_file.read_text().splitlines()

    antennas = find_antennas(map)

    x = [
        x
        for antennas_freq in antennas.values()
        for a, b in combinations(antennas_freq, 2)
        for x in find_antinodes(a, b)
        if in_map(map, x) and x not in antennas_freq
    ]
    print(x)
    print(len(set(x)))


if __name__ == "__main__":
    main()
