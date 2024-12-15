import enum
from itertools import pairwise, tee
from pathlib import Path
from turtle import position, width
from typing import List, Tuple, Dict, Set
import re
from collections import Counter
from dataclasses import dataclass
from colorama import Fore, Back, Style

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIRECTION_MAP = {
    "^": (0, -1),
    "v": (0, 1),
    ">": (1, 0),
    "<": (-1, 0),
}


def draw(walls, blocks, robot, width, height):
    for i in range(height):
        for j in range(width):
            x = "."
            if (j, i) in walls:
                x = "#"
            if (j, i) in blocks:
                x = "O"
            if (j, i) == robot:
                x = "@"
            print(x, end="")

        print("")


def move(
    walls: Set[Tuple[int, int]],
    blocks: Set[Tuple[int, int]],
    robot: Tuple[int, int],
    direction,
):
    d = DIRECTION_MAP[direction]

    ret: Set[Tuple[int, int]] = set()
    next_robot = robot[0] + d[0], robot[1] + d[1]
    i = next_robot
    while True:
        if i in walls:
            return walls, blocks, robot
        if i not in blocks:
            break
        ret.add(i)
        i = i[0] + d[0], i[1] + d[1]

    new_ret: Set[Tuple[int, int]] = {(b[0] + d[0], b[1] + d[1]) for b in ret}
    return walls, blocks - ret | new_ret, next_robot


def main():
    file = Path(__file__).parent / "input"
    # file = Path(__file__).parent / "example"

    map, actions = file.read_text().split("\n\n")

    map = map.splitlines()
    height = len(map)
    width = len(map[0])

    walls = {
        (x, y) for y, line in enumerate(map) for x, c in enumerate(line) if c == "#"
    }
    blocks = {
        (x, y) for y, line in enumerate(map) for x, c in enumerate(line) if c == "O"
    }
    robot = [
        (x, y) for y, line in enumerate(map) for x, c in enumerate(line) if c == "@"
    ]
    assert len(robot) == 1
    robot = robot[0]

    # draw(walls, blocks, robot, width, height)
    # input()

    for action in actions:
        if action in DIRECTION_MAP:
            walls, blocks, robot = move(walls, blocks, robot, action)
            # draw(walls, blocks, robot, width, height)
            # input()

    draw(walls, blocks, robot, width, height)
    print(sum(x + 100 * y for x, y in blocks))


if __name__ == "__main__":
    main()
