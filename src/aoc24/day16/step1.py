from itertools import pairwise, chain
from pathlib import Path
from typing import List, Tuple, Dict
from colorama import Fore, Style
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
    return (
        len(path)
        - 1
        + sum(
            1000
            for a, b in pairwise(
                chain([(1, 0)], ((b[0] - a[0], b[1] - a[1]) for a, b in pairwise(path)))
            )
            if a != b
        )
    )


def main():
    file, expected = Path(__file__).parent / "input", None
    # file, expected = Path(__file__).parent / "example", 7036
    # file, expected = Path(__file__).parent / "example_2", 11048

    maze = file.read_text().splitlines()

    start = find_point(maze, "S")
    end = find_point(maze, "E")

    if start is None or end is None:
        raise ValueError("Start or end not found")

    heap: List[Tuple[int, Tuple[int, int], List[Tuple[int, int]]]] = [
        (0, start, [start])
    ]
    min_map: Dict[Tuple[Tuple[int, int], Tuple[int, int]], int] = {}

    i = 0
    while True:
        score, pos, path = heapq.heappop(heap)

        i += 1
        if i % 10000 == 0:
            print(i, score, len(heap))
            # draw(maze, path)

        if pos == end:
            draw(maze, path)
            if expected is not None:
                assert score_path(path) == expected, (
                    score_path(path),
                    expected,
                )
            print("Found", score_path(path))
            return

        for d in DIRECTIONS:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if maze[new_pos[1]][new_pos[0]] == "#":
                continue
            if new_pos in path:
                continue

            new_path = path + [new_pos]
            new_score = score_path(new_path)

            key = (new_pos, d)
            if (key in min_map) and (new_score >= min_map[key]):
                continue

            min_map[key] = new_score

            # Attempt 2
            # if new_score >= 105512:
            #    continue

            heapq.heappush(heap, (new_score, new_pos, new_path))


if __name__ == "__main__":
    main()
