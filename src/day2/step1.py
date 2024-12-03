from pathlib import Path
from typing import List
from itertools import pairwise


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


def main():
    file = Path(__file__).parent / "input"

    count = len(
        list(
            filter(
                differ_by_1_to_3,
                filter(
                    is_monotonic, map(line_to_num_array, file.read_text().splitlines())
                ),
            )
        )
    )
    print("Count: ", count)


if __name__ == "__main__":
    main()
