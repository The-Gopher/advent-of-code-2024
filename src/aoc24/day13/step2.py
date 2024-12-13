from itertools import pairwise, tee
from pathlib import Path
from typing import List, Tuple, Dict
import re

LINE_REGEX = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"


# a*ax + b*bx = px
# a = (px - b*bx) / ax

# a*ay + b*by = py
# a = (py - b*by) / ay

# (px - b*bx) / ax = (py - b*by) / ay
# (px - b*bx)*ay = (py - b*by)*ax
# px*ay - b*bx*ay = py*ax - b*by*ax
# px*ay - py*ax = b*bx*ay  - b*by*ax
# px*ay - py*ax = b * (bx*ay  - by*ax)
# (px*ay - py*ax) / (bx*ay  - by*ax) = b


def main():
    file = Path(__file__).parent / "input"
    # file = Path(__file__).parent / "example"
    # file = Path(__file__).parent / "example_1"

    data = file.read_text().strip()

    total = 0

    for case in re.findall(LINE_REGEX, data):
        ax, ay, bx, by, px, py = map(int, case)

        px += 10000000000000
        py += 10000000000000

        num = px * ay - py * ax
        den = bx * ay - by * ax

        b = num // den
        if num % den != 0:
            # print("Not Found", num, den, num // den, num % den)
            continue

        a = (px - b * bx) // ax

        if a * ax + b * bx == px and a * ay + b * by == py:
            total += 3 * a + b
        else:
            print(
                "-- Not Found --",
                num,
                den,
                num // den,
                num % den,
                px - a * ax - b * bx,
                py - a * ay - b * by,
            )

    assert total != 77779103984288
    print("total", total)


if __name__ == "__main__":
    main()
