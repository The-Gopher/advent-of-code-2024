from re import findall
from typing import List, Tuple
from pathlib import Path

MUL_REGEX = r"mul\((\d{1,3}),(\d{1,3})\)"


def find_multiplications(string) -> List[Tuple[int, int]]:
    return [(int(a), int(b)) for a, b in findall(MUL_REGEX, string)]


def main():
    input_file = Path(__file__).parent / "input"
    total = 0
    for a, b in find_multiplications(input_file.read_text()):
        total += a * b
    print(total)


if __name__ == "__main__":
    main()
