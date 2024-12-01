from pathlib import Path


def main():
    input = Path(__file__).parent / "input"

    lines = input.read_text().splitlines()
    list_a = sorted([int(x.split("   ")[0]) for x in lines])
    list_b = sorted([int(x.split("   ")[1]) for x in lines])
    diff = [abs(x - y) for x, y in zip(list_a, list_b)]
    sum_diff = sum(diff)
    
    print(sum_diff)


if __name__ == "__main__":
    main()
