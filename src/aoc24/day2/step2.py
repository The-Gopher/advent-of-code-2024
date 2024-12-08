from pathlib import Path
from typing import List, Literal
from itertools import count, pairwise
from collections import Counter


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


def dapended_pairwise_comparisons_safe(
    comparisons: List[tuple[Literal["U"] | Literal["E"] | Literal["D"], int]],
) -> bool:
    if len({dir for dir, _ in comparisons}) == 1 and all(
        0 < diff < 4 for _, diff in comparisons
    ):
        return True

    minus_first = comparisons[1:]
    if len({dir for dir, _ in minus_first}) == 1 and all(
        0 < diff < 4 for _, diff in minus_first
    ):
        return True

    minus_last = comparisons[:-1]
    if len({dir for dir, _ in minus_last}) == 1 and all(
        0 < diff < 4 for _, diff in minus_last
    ):
        return True

    if len({dir for dir, _ in comparisons}) == 1:
        # Monotonic and first and last are not the problems elements so this cannnot be fixed based on dropping an element
        return False

    dir_counts = Counter(dir for dir, _ in comparisons)
    if len(dir_counts) > 2 and dir_counts.most_common(2)[1][1] > 1:
        # Two out of direction so this cannot be fixed by dropping a single element
        return False

    most_common_dir, _ = dir_counts.most_common(1)[0]
    if most_common_dir == "E":
        return False

    to_remove = []
    for a, b in pairwise(comparisons):
        dir_a, diff_a = a
        dir_b, diff_b = b

        if most_common_dir != dir_b and abs(diff_a - diff_b) < 3:
            to_remove.append(a)

    if len(to_remove) == 1:
        return True

    return False


def main():
    file = Path(__file__).parent / "input"
    # file = Path(__file__).parent / "example"

    readings = [
        [int(x) for x in line.split(" ")] for line in file.read_text().splitlines()
    ]

    print(
        len(
            [
                x
                for x in readings
                if pairwise_comparisons_safe(
                    [pairwise_test(a, b) for a, b in pairwise(x)]
                )
            ]
        )
    )


if __name__ == "__main__":
    main()
