from pathlib import Path
from typing import List, Literal
from itertools import pairwise


def pairwise_test(a: int, b: int) -> tuple[Literal["U"] | Literal["D"], int]:
    return ("U" if a < b else "D", abs(a - b))


def pairwise_comparisons_safe(
    comparisons: List[tuple[Literal["U"] | Literal["D"], int]],
) -> bool:
    if len({dir for dir, _ in comparisons}) == 1 and all(
        0 < diff < 4 for _, diff in comparisons
    ):
        return True

    return False


def main():
    file = Path(__file__).parent / "input"
    file = Path(__file__).parent / "example"

    readings = [
        [int(x) for x in line.split(" ")] for line in file.read_text().splitlines()
    ]

    pairwise_comparisons = [
        [pairwise_test(a, b) for a, b in pairwise(reading)] for reading in readings
    ]

    for comparisons in pairwise_comparisons:
        print(pairwise_comparisons_safe(comparisons))


if __name__ == "__main__":
    main()
