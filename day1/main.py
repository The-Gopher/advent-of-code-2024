from pathlib import Path
from collections import Counter


def step1():
    input = Path(__file__).parent / "input"

    lines = input.read_text().splitlines()
    list_a = sorted([int(x.split("   ")[0]) for x in lines])
    list_b = sorted([int(x.split("   ")[1]) for x in lines])
    diff = [abs(x - y) for x, y in zip(list_a, list_b)]
    sum_diff = sum(diff)

    print(sum_diff)


def step2():
    input = Path(__file__).parent / "input"

    lines = input.read_text().splitlines()
    list_a = sorted([int(x.split("   ")[0]) for x in lines])
    list_b = sorted([int(x.split("   ")[1]) for x in lines])

    counts_b = Counter(list_b)

    weighted = [x * counts_b[x] for x in list_a]

    print(sum(weighted))


if __name__ == "__main__":
    step2()
