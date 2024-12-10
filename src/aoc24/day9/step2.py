from pathlib import Path
from typing import List, Tuple
from dataclasses import dataclass

EXAMPLE_EXPANED = [
    int(x) if x != "." else None for x in "00...111...2...333.44.5555.6666.777.888899"
]


@dataclass
class FileSystemFile:
    file_id: int
    file_size: int


def expand_line(line: str) -> List[FileSystemFile | None]:
    ret: List[FileSystemFile | None] = []

    block_index = 0
    has_data = True

    has_data = False
    start = 0
    for character in line:
        has_data = not has_data
        size = int(character)
        if size != 0:
            block = FileSystemFile(block_index, size) if has_data else None

            for i in range(size):
                ret.append(block)
                start += 1
        if has_data:
            block_index += 1
    return ret


def compress_line(line: List[FileSystemFile | None]):
    end = len(line) - 1

    def find_first_free_segment(
        line: List[FileSystemFile | None], size: int
    ) -> None | int:
        i = 0
        while i < len(line) - 1:
            if line[i] is not None:
                i += line[i].file_size
            elif (
                line[i] is None
                and all([x is None for x in line[i : i + size]])
                and i + size < len(line)
            ):
                return i
            else:
                i += 1
        return None

    while end > 0:
        print(end)
        # print_block(line)

        value = line[end]
        if value is None:
            end -= 1
        else:
            new_start = find_first_free_segment(line, value.file_size)
            # print_loc(new_start)
            if new_start and new_start < end:
                for i in range(value.file_size):
                    line[new_start + i] = value
                    line[end - i] = None
            end -= value.file_size

    return line


def print_block(line: List[FileSystemFile | None]):
    for i, x in enumerate(line):
        if x is None:
            print(".", end="")
        else:
            print(x.file_id, end="")
    print()


def print_loc(loc: int | None):
    if loc:
        print(" " * loc + "^")


def checksum_line(line: List[FileSystemFile | None]) -> int:
    return sum(idx * x.file_id for idx, x in enumerate(line) if x is not None)


def main():
    file = Path(__file__).parent / "input"
    # file = Path(__file__).parent / "example"

    expanded = expand_line(file.read_text())
    compress_line(expanded)
    print_block(expanded)
    checksum = checksum_line(expanded)
    print(checksum)


if __name__ == "__main__":
    main()
