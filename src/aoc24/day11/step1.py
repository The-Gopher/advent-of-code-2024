from pathlib import Path
from turtle import st
from typing import List, Set, Tuple


def step(in_list: List[int]) -> List[int]:
    def func(x: int) -> List[int]:
        if x == 0:
            return [1]
        elif len(str(x)) % 2 == 0:
            left, right = str(x)[: len(str(x)) // 2], str(x)[len(str(x)) // 2 :]
            left_strp, right_strp = left.lstrip("0"), right.lstrip("0")
            if left_strp == "":
                left_strp = "0"
            if right_strp == "":
                right_strp = "0"
            return [int(left_strp), int(right_strp)]
        else:
            return [x * 2024]

    return [x for y in in_list for x in func(y)]


def main():
    x = STEP_0
    for i in range(25):
        x = step(x)
    print(len(x))

    x = [112, 1110, 163902, 0, 7656027, 83039, 9, 74]
    for i in range(25):
        x = step(x)
    print(len(x))


STEP_0 = [125, 17]
STEP_1 = [253000, 1, 7]
STEP_2 = [253, 0, 2024, 14168]
STEP_3 = [512072, 1, 20, 24, 28676032]

assert step(STEP_0) == STEP_1, step(STEP_0)
assert step(STEP_1) == STEP_2, step(STEP_1)
assert step(STEP_2) == STEP_3, step(STEP_2)

if __name__ == "__main__":
    main()