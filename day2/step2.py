from pathlib import Path
from typing import List
from utils import nwise

def is_monotonic(nums: List[int]) -> bool:
    first = nums[0]
    for a, b in nwise(nums[1:]):
        if first <= a <= b:
            continue
        if first >= a >= b:
            continue
        return False
    return True


def differ_by_1_to_3(nums: List[int]) -> bool:
    for a, b in nwise(nums):
        if abs(b - a) not in (1, 2, 3):
            return False
    return True


def line_dampended_safe(line_nums: List[int]) -> bool:
    for a, b, c in nwise(line_nums, 3, 3):

        if a == b == c:
            return False
    if not is_monotonic(line_nums):
        return False
    if not differ_by_1_to_3(line_nums):
        return False
    return True


def line_is_safe(line: str) -> bool:
    line_nums = [int(x) for x in line.split()]
    if is_monotonic(line_nums) and differ_by_1_to_3(line_nums):
        return True
    if line_dampended_safe(line_nums):
        return True
    return False


def main():
    file = Path(__file__).parent / "input"

    count = len(list(filter(line_is_safe, file.read_text().splitlines())))
    print("Count: ", count)


if __name__ == "__main__":
    main()
