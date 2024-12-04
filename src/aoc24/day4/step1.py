import enum
from pathlib import Path
from typing import List

DIRECTIONS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def main():
    search_text = "XMAS"
    file = Path(__file__).parent / "input"
    file_content: List[str] = file.read_text().splitlines()

    def get_character(x, y) -> str | None:
        if y < 0 or y >= len(file_content):
            return None

        if x < 0 or x >= len(file_content[y]):
            return None

        return file_content[y][x]

    def matches(x, y, direction) -> bool:
        for i, c in enumerate(search_text):
            if get_character(x + direction[0] * i, y + direction[1] * i) != c:
                return False
        return True

    total = 0
    for y in range(len(file_content)):
        for x in range(len(file_content[y])):
            for direction in DIRECTIONS:
                if matches(x, y, direction):
                    total += 1

    print(total)


if __name__ == "__main__":
    main()
