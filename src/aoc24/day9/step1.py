from pathlib import Path
from typing import List


EXAMPLE_EXPANED = [
    int(x) if x != "." else None for x in "00...111...2...333.44.5555.6666.777.888899"
]


def expand_line(line: str) -> List[int | None]:
    ret: List[int | None] = []

    block_index = 0
    has_data = True

    for character in line:
        for i in range(int(character)):
            ret.append(block_index if has_data else None)

        if has_data:
            block_index += 1
        has_data = not has_data
    return ret


def compress_line(line: List[int | None]) -> List[int | None]:
    start, end = 0, len(line) - 1

    while start < end:
        if line[start] is not None:
            start += 1
        elif line[end] is None:
            end -= 1
        else:
            line[start] = line[end]
            line[end] = None
            start += 1
            end -= 1

    return line


def checksum_line(line: List[int | None]) -> int:
    return sum(idx * x for idx, x in enumerate(line) if x is not None)


def main():
    file = Path(__file__).parent / "input"
    # file = Path(__file__).parent / "example"

    expanded = expand_line(file.read_text())
    compressed = compress_line(expanded)
    checksum = checksum_line(compressed)
    print(checksum)


if __name__ == "__main__":
    main()
