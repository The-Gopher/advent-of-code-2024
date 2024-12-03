from re import findall
from typing import List, Tuple
from pathlib import Path

MUL_REGEX = r"mul\((\d{1,3}),(\d{1,3})\)"
DOES_REGEX = r"""(^|do\(\)|don\'t\(\))(.+?)(?=$|do\(\)|don\'t\(\))"""


def find_dos(string) -> List[str]:
    return [b for a, b in findall(DOES_REGEX, string) if a in ("", "do()")]


def find_sections(string) -> List[str]:
    return findall(DOES_REGEX, string)


def find_multiplications(string) -> List[Tuple[int, int]]:
    return [(int(a), int(b)) for a, b in findall(MUL_REGEX, string)]


def main():
    input_file = Path(__file__).parent / "input"
    does = find_dos(input_file.read_text())
    multiplications = [
        (a * b) for do_section in does for a, b in find_multiplications(do_section)
    ]
    print(sum(multiplications))


if __name__ == "__main__":
    main()
