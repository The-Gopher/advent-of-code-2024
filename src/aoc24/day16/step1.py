from itertools import pairwise, chain
from pathlib import Path
from typing import List, Tuple, Dict, Set
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


def draw(maze: List[str], path: Set[Tuple[int, int]]):
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
    # file, expected = Path(__file__).parent / "example_2", 11048
    # file, expected = Path(__file__).parent / "example", 7036

    maze = file.read_text().splitlines()

    start = find_point(maze, "S")
    end = find_point(maze, "E")

    if start is None or end is None:
        raise ValueError("Start or end not found")

    heap: List[Tuple[int, Tuple[int, int], List[Tuple[int, int]]]] = [
        (0, start, [start])
    ]

    min_map: Dict[Tuple[Tuple[int, int], Tuple[int, int]], int] = {}

    best_paths: List[List[Tuple[int, int]]] = []
    best_score = None

    while True:
        score, pos, path = heapq.heappop(heap)

        if best_score and score > best_score:
            break

        if pos == end:
            assert score == score_path(path)
            best_score = score
            best_paths.append(path)

        for d in DIRECTIONS:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if maze[new_pos[1]][new_pos[0]] == "#":
                continue
            if new_pos in path:
                continue

            new_path = path + [new_pos]
            new_score = score_path(new_path)

            key = (new_pos, d)
            if (key in min_map) and (new_score > min_map[key]):
                continue
            min_map[key] = new_score

            heapq.heappush(heap, (new_score, new_pos, new_path))

    print(best_score)
    print(len(set(tile for path in best_paths for tile in path)))


if __name__ == "__main__":
    main()
