from pathlib import Path
from typing import List, Literal
from itertools import count, pairwise
from collections import Counter
from xmlrpc.client import Boolean


def pairwise_test(
    a: int, b: int
) -> tuple[Literal["U"] | Literal["E"] | Literal["D"], int]:
    if a > b:
        dir = "D"
    elif a < b:
        dir = "U"
    else:
        dir = "E"
    diff = abs(a - b)

    return (dir, diff)


def pairwise_comparisons_safe(
    comparisons: List[tuple[Literal["U"] | Literal["E"] | Literal["D"], int]],
) -> bool:
    if len({dir for dir, _ in comparisons}) == 1 and all(
        0 < diff < 4 for _, diff in comparisons
    ):
        return True

    return False


def safe_reading(reading: List[int]) -> bool:
    pairwise_comparisons = [pairwise_test(a, b) for a, b in pairwise(reading)]
    if pairwise_comparisons_safe(pairwise_comparisons):
        return True

    for i in range(len(reading)):
        pairwise_comparisons = [
            pairwise_test(a, b) for a, b in pairwise(reading[:i] + reading[i + 1 :])
        ]
        if pairwise_comparisons_safe(pairwise_comparisons):
            return True
    return False


def main():
    file = Path(__file__).parent / "input"
    # file = Path(__file__).parent / "example"

    readings = [
        [int(x) for x in line.split(" ")] for line in file.read_text().splitlines()
    ]

    print(len([x for x in readings if safe_reading(x)]))


if __name__ == "__main__":
    main()
