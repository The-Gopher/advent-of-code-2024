import enum
from itertools import pairwise, tee
from pathlib import Path
from turtle import pos, position, width
from typing import List, Tuple, Dict, Set
import re
from collections import Counter
from dataclasses import dataclass
from colorama import Fore, Back, Style
import heapq

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIRECTION_MAP = {
    "^": (0, -1),
    "v": (0, 1),
    ">": (1, 0),
    "<": (-1, 0),
}


def find_point(maze: List[str], point: str) -> Tuple[int, int] | None:
    for y, line in enumerate(maze):
        x = line.find(point)
        if x != -1:
            return x, y
    return None


def draw(maze: List[str], path: List[Tuple[int, int]]):
    for y, line in enumerate(maze):
        for x, c in enumerate(line):
            if (x, y) in path:
                print(Fore.RED + c + Fore.RESET, end="")
            else:
                print(c, end="")
        print(Style.RESET_ALL)


def score_path(path: List[Tuple[int, int]]) -> int:
    turn_score = sum(
        1000
        for a, b in pairwise((a[0] - b[0], a[1] - b[1]) for a, b in pairwise(path))
        if a != b
    )
    return len(path) + turn_score


def main():
    file = Path(__file__).parent / "input"
    # file = Path(__file__).parent / "example"

    maze = file.read_text().splitlines()

    start = find_point(maze, "S")
    end = find_point(maze, "E")

    if start is None or end is None:
        raise ValueError("Start or end not found")

    heap: List[Tuple[int, Tuple[int, int], Tuple[int, int], List[Tuple[int, int]]]] = [
        (0, start, (0, 1), [])
    ]

    i = 0
    while True:
        score, pos, last_dir, path = heapq.heappop(heap)

        i += 1
        if i % 10000 == 0:
            print(i, score)
            draw(maze, path)

        for d in DIRECTIONS:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if new_pos == end:
                new_path = path + [new_pos]

                draw(maze, new_path)
                print("Found", score_path(new_path) + 1000)
                return
            if maze[new_pos[1]][new_pos[0]] == "#":
                continue
            if new_pos in path:
                continue

            new_path = path + [new_pos]
            new_score = (
                score_path(new_path)
                + abs(new_pos[0] - end[0])
                + abs(new_pos[1] - end[1])
            )
            heapq.heappush(heap, (new_score, new_pos, d, new_path))


if __name__ == "__main__":
    main()
