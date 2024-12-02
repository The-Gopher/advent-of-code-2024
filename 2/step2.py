from pathlib import Path
from typing import List
from itertools import pairwise


def nwise(iterable, window_size=2, min_item_count=2):
    x = [None] * (window_size - min_item_count) + iterable[:min_item_count]
    yield x
    for y in iterable[min_item_count:]:
        x = x[1:] + [y]
        yield x
    for _ in range(window_size - min_item_count):
        x = x[1:] + [None]
        yield x


def is_monotonic(nums: List[int]) -> bool:
    first = nums[0]
    for a, b in pairwise(nums[1:]):
        if first <= a <= b:
            continue
        if first >= a >= b:
            continue
        return False
    return True


def differ_by_1_to_3(nums: List[int]) -> bool:
    for a, b in pairwise(nums):
        if abs(b - a) not in (1, 2, 3):
            return False
    return True


def line_to_num_array(line: str) -> List[int]:
    return [int(x) for x in line.split()]


def line_is_safe(line: str) -> bool:
    line_nums = [int(x) for x in line.split()]
    if not is_monotonic(line_nums):
        return False
    if not differ_by_1_to_3(line_nums):
        return False
    return True


def main():
    file = Path(__file__).parent / "input"

    count = len(list(filter(line_is_safe, file.read_text().splitlines())))
    print("Count: ", count)


if __name__ == "__main__":
    main()
