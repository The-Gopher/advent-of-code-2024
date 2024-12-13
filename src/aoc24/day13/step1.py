from itertools import pairwise, tee
from pathlib import Path
from typing import List, Tuple, Dict
import re

LINE_REGEX = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"


# a*ax + b*bx = px
# a*ay + b*by = py


def main():
    file = Path(__file__).parent / "input"
    # file = Path(__file__).parent / "example"
    # file = Path(__file__).parent / "example_1"

    data = file.read_text().strip()

    total = 0

    for case in re.findall(LINE_REGEX, data):
        ax, ay, bx, by, px, py = map(int, case)

        a = 0
        while a * ax <= px:
            aax = a * ax
            aay = a * ay
            b = 0
            while aax + b * bx <= px:
                if aay + b * by == py and aax + b * bx == px:
                    print("found", a, b)
                    total += 3 * a + b
                b += 1
            a += 1
    print("total", total)


if __name__ == "__main__":
    main()
