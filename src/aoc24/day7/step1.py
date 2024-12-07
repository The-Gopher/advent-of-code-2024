from pathlib import Path
from enum import Enum


def processes(target_value: int, running_value: int, rest: list[int]) -> int:

    if running_value == target_value and len(rest) == 0:
        return True

    if running_value > target_value or len(rest) == 0:
        return False

    first, *rest = rest
    if processes(target_value, running_value + first, rest):
        return True
    if processes(target_value, running_value * first, rest):
        return True

    return False


def main():
    input_file = Path(__file__).parent / "input"
    # input_file = Path(__file__).parent / "example"

    total_sum = 0

    for line in input_file.read_text().splitlines():
        line_sum, rest = line.split(": ")
        line_sum = int(line_sum)
        line_values = [int(x) for x in rest.split(" ")]
        first, *rest = line_values
        if processes(line_sum, first, rest):
            total_sum += line_sum

    print(total_sum)


if __name__ == "__main__":

    main()
