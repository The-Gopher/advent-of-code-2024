from multiprocessing import Value
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


def start_node(in_edges) -> str:
    for page, in_edges in in_edges.items():
        if len(in_edges) == 0:
            return page
    raise ValueError("No start node found")


def correct_ordering(out_edges: dict[str, set], page_line) -> str:
    pages = set(page_line.split(","))

    out_edges_subset: dict[str, set] = {}
    for page in pages:
        out_edges_subset[page] = out_edges[page] & pages

    correct_order = []
    while len(out_edges_subset) > 0:
        next_node = start_node(out_edges_subset)
        correct_order.append(next_node)

        out_edges_subset = {
            k: v - {next_node} for k, v in out_edges_subset.items() if k != next_node
        }

    return ",".join(correct_order)


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
        if not is_valid(in_edges, line):
            corrected_line = correct_ordering(out_edges, line)
            pages = corrected_line.split(",")
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
