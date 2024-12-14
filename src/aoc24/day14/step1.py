from itertools import pairwise, tee
from pathlib import Path
from turtle import position, width
from typing import List, Tuple, Dict
import re
from collections import Counter
from dataclasses import dataclass

PARSE_LINE = r"p=(.+),(.+) v=(.+),(.+)"


@dataclass
class Robot:
    x: int
    y: int
    dx: int
    dy: int


def draw_grid(width: int, height: int, grid: List[Tuple[int, int]]):
    counts = Counter(grid)
    for y in range(height):
        print(f"{y:03d} ", end="")
        if 2 * y == height - 1:
            print("")
            continue

        for x in range(width):
            if 2 * x == width - 1:
                print(" ", end="")
                continue

            print(counts[(x, y)] or ".", end="")
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


def main():
    file = Path(__file__).parent / "input"
    t = 100
    width = 101
    height = 103

    # file = Path(__file__).parent / "example"
    # t = 100
    # width = 11
    # height = 7

    data = file.read_text().splitlines()
    robots = [Robot(*map(int, re.match(PARSE_LINE, line).groups())) for line in data]

    positions = [((r.x + t * r.dx) % width, (r.y + t * r.dy) % height) for r in robots]
    draw_grid(width, height, positions)

    x_mid = (width) // 2
    y_mid = (height) // 2

    print(x_mid, y_mid)

    q1 = [p for p in positions if p[0] < x_mid and p[1] < y_mid]
    q2 = [p for p in positions if p[0] > x_mid and p[1] < y_mid]
    q3 = [p for p in positions if p[0] < x_mid and p[1] > y_mid]
    q4 = [p for p in positions if p[0] > x_mid and p[1] > y_mid]

    print(f"Total: {len(q1) * len(q2) * len(q3) * len(q4)}")


if __name__ == "__main__":
    main()
