from pathlib import Path
from typing import List



def main():
    file = Path(__file__).parent / "input"
    file_content: List[str] = file.read_text().splitlines()

    def get_character(x, y) -> str | None:
        if y < 0 or y >= len(file_content):
            return None

        if x < 0 or x >= len(file_content[y]):
            return None

        return file_content[y][x]

    def matches(x, y) -> bool:
        if {get_character(x + 1, y + 1), get_character(x - 1, y - 1)} != {"M", "S"}:
            return False
        if {get_character(x + 1, y - 1), get_character(x - 1, y + 1)} != {"M", "S"}:
            return False
        return True

    total = 0
    for y in range(len(file_content)):
        for x in range(len(file_content[y])):
            if get_character(x, y) == "A":
                if matches(x, y):
                    total += 1
                pass

    print(total)


if __name__ == "__main__":
    main()
