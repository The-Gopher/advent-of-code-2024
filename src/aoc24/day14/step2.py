from itertools import pairwise, tee
from pathlib import Path
from turtle import position, width
from typing import List, Tuple, Dict
import re
from collections import Counter
from dataclasses import dataclass

PARSE_LINE = r"p=(.+),(.+) v=(.+),(.+)"
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


@dataclass
class Robot:
    x: int
    y: int
    dx: int
    dy: int


def draw_grid(width: int, height: int, grid: List[Tuple[int, int]], split=True):
    counts = Counter(grid)
    for y in range(height):
        print(f"{y:03d} ", end="")
        if 2 * y == height - 1 and split:
            print("")
            continue

        for x in range(width):
            if 2 * x == width - 1 and split:
                print(" ", end="")
                continue

            print(counts[(x, y)] or " ", end="")
        print()


def test():
    file = Path(__file__).parent / "example_1"
    t = 6
    width = 11
    height = 7

    data = file.read_text().splitlines()
    robots = [Robot(*map(int, re.match(PARSE_LINE, line).groups())) for line in data]

    for i in range(t):
        print("")
        print(f"Time: {i}")
        positions = [
            ((r.x + i * r.dx) % width, (r.y + i * r.dy) % height) for r in robots
        ]
        draw_grid(width, height, positions)


def count_neighbours(grid: List[Tuple[int, int]]):
    count = 0
    for ppos in grid:
        for dir in DIRECTIONS:
            new_p = (ppos[0] + dir[0], ppos[1] + dir[1])
            if new_p in grid:
                count += 1
    return count


def main():
    file = Path(__file__).parent / "input"
    t = 100
    width = 101
    height = 103

    data = file.read_text().splitlines()
    robots = [Robot(*map(int, re.match(PARSE_LINE, line).groups())) for line in data]

    x_mid = (width) // 2

    i = 0
    last_max = 0
    while i < 10_000:
        i += 1

        positions = [
            ((r.x + i * r.dx) % width, (r.y + i * r.dy) % height) for r in robots
        ]
        neightbours = count_neighbours(positions)
        if neightbours >= last_max:
            last_max = neightbours
            print("")
            print(f"Time: {i}")
            draw_grid(width, height, positions, False)


if __name__ == "__main__":
    main()
