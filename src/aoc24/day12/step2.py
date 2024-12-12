from pathlib import Path
from typing import List, Tuple, Dict

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def split_into_groups(data: List[str]) -> Dict[Tuple[int, int], str]:
    ret = {}
    for y_idx, line in enumerate(data):
        for x_idx, char in enumerate(line):
            ret[(x_idx, y_idx)] = char
    return ret


def remove_if_in(in_set, value) -> bool:
    if value in in_set:
        in_set.remove(value)
        return True
    return False


def get_perimter(points: List[Tuple[int, int]]) -> int:
    perimeter = 0
    x = {
        (d, p)
        for p in points
        for d in DIRECTIONS
        if (p[0] + d[0], p[1] + d[1]) not in points
    }

    while x:
        perimeter += 1
        d, p = x.pop()

        d_right = (d[1], -d[0])
        idx = 1
        while remove_if_in(x, (d, (p[0] + d_right[0] * idx, p[1] + d_right[1] * idx))):
            idx += 1

        d_left = (-d[1], d[0])
        idx = 1
        while remove_if_in(x, (d, (p[0] + d_left[0] * idx, p[1] + d_left[1] * idx))):
            idx += 1

    return perimeter


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
