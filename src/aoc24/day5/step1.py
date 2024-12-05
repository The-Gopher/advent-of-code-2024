from operator import inv
from pathlib import Path
from collections import defaultdict


def is_valid(in_edges, page_line) -> bool:
    pages = page_line.split(",")

    invalid_pages = set()
    for page in pages:
        if page in invalid_pages:
            return False
        invalid_pages |= in_edges[page]
    return True


def main():
    input_file = Path(__file__).parent / "input"
    requirements, tests = input_file.read_text().split("\n\n")

    out_edges = defaultdict(set)
    in_edges = defaultdict(set)

    for line in requirements.splitlines():
        x, y = line.split("|")
        out_edges[x].add(y)
        in_edges[y].add(x)

    sum = 0
    for line in tests.splitlines():
        if is_valid(in_edges, line):
            pages = line.split(",")
            middle = pages[len(pages) // 2]
            sum += int(middle)
    print(sum)


    """
    assert is_valid(in_edges, "75,47,61,53,29")
    assert is_valid(in_edges, "97,61,53,29,13")
    assert is_valid(in_edges, "75,29,13")

    assert not is_valid(in_edges, "75,97,47,61,53")
    assert not is_valid(in_edges, "61,13,29")
    assert not is_valid(in_edges, "97,13,75,29,47")
    """

if __name__ == "__main__":
    main()
