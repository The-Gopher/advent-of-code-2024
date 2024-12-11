from pathlib import Path
from turtle import st
from typing import List, Set, Tuple, Dict


EXAMPLE_STEP_0 = [125, 17]
STEP_1 = [253000, 1, 7]
STEP_2 = [253, 0, 2024, 14168]
STEP_3 = [512072, 1, 20, 24, 28676032]

INPUT_STEP_0 = [112, 1110, 163902, 0, 7656027, 83039, 9, 74]


MAP: Dict[Tuple[int, int], int] = dict()


def count_stone_expansion(num: int, depth_to_go: int) -> int:
    if (num, depth_to_go) in MAP:
        return MAP[(num, depth_to_go)]
    ret = do_count_stone_expansion(num, depth_to_go)
    MAP[(num, depth_to_go)] = ret
    return ret


def do_count_stone_expansion(num: int, depth_to_go: int) -> int:
    if depth_to_go == 0:
        return 1

    if num == 0:
        return count_stone_expansion(1, depth_to_go - 1)

    str_num = str(num)
    len_num = len(str_num)
    if len_num % 2 == 0:
        left, right = str_num[: len_num // 2], str_num[len_num // 2 :]
        left_strp, right_strp = left.lstrip("0"), right.lstrip("0")
        if left_strp == "":
            left_strp = "0"
        if right_strp == "":
            right_strp = "0"
        return count_stone_expansion(
            int(left_strp), depth_to_go - 1
        ) + count_stone_expansion(int(right_strp), depth_to_go - 1)

    return count_stone_expansion(num * 2024, depth_to_go - 1)


def count_stones(x: List[int], depth_to_go: int) -> int:

    sum = 0
    for num in x:
        sum += count_stone_expansion(num, depth_to_go)
    return sum


def main():
    print(count_stones(EXAMPLE_STEP_0, 75))
    print(count_stones(INPUT_STEP_0, 75))


assert count_stones(EXAMPLE_STEP_0, 25) == 55312


if __name__ == "__main__":
    main()
