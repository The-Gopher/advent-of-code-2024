from itertools import pairwise, tee
from pathlib import Path
from typing import List, Tuple, Dict

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def split_into_groups(data: List[str]) -> Dict[Tuple[int, int], str]:
    ret = {}
    for y_idx, line in enumerate(data):
        for x_idx, char in enumerate(line):
            ret[(x_idx, y_idx)] = char
    return ret


def pairwise_wrap(iterable):
    first_iter, main_iter = tee(iterable, 2)
    first = next(first_iter)

    for a, b in pairwise(main_iter):
        yield a, b
    yield b, first


def get_perimter(points: List[Tuple[int, int]]) -> int:
    point_set = set(points)
    corner = 0
    for p in point_set:
        for a, b in pairwise_wrap(DIRECTIONS):
            p_a = (p[0] + a[0], p[1] + a[1])
            p_b = (p[0] + b[0], p[1] + b[1])
            p_ab = (p[0] + a[0] + b[0], p[1] + a[1] + b[1])
            # Convex corner
            if p_a not in point_set and p_b not in point_set:
                corner += 1
            # Concave corner
            if p_a in point_set and p_b in point_set and p_ab not in point_set:
                corner += 1
    return corner


def main():
    file = Path(__file__).parent / "input"
    # file = Path(__file__).parent / "example"
    # file = Path(__file__).parent / "example_1"

    file_data = file.read_text().splitlines()
    data = split_into_groups(file_data)
    print(len(file_data), len(file_data[0]), len(data))

    total = 0

    while data:
        p, p_v = data.popitem()
        group_points: List[Tuple[int, int]] = [p]

        i = 0
        while i < len(group_points):
            p = group_points[i]
            for dir in DIRECTIONS:
                new_p = (p[0] + dir[0], p[1] + dir[1])
                if new_p in data and data[new_p] == p_v:
                    group_points.append(new_p)
                    data.pop(new_p)

            i += 1
        area = len(group_points)
        perimeter = get_perimter(group_points)
        total += area * perimeter

    print("total", total)


if __name__ == "__main__":
    main()
