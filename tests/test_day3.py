from aoc24.day3.step1 import find_multiplications
from aoc24.day3.step2 import find_sections, find_dos


def test_step1():
    string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert find_multiplications(string) == [(2, 4), (5, 5), (11, 8), (8, 5)]


def test_dos_start_to_do():
    test_string = "abcdo()efg"
    assert find_sections(test_string)[0] == ("", "abc")


def test_dos_start_to_dont():
    test_string = "abcdon't()efg"
    assert find_sections(test_string)[0] == ("", "abc")


def test_dos_end_to_do():
    test_string = "abcdo()efgdo()"
    assert find_sections(test_string) == [("", "abc"), ("do()", "efg")]


def test_dos_end_to_dont():
    test_string = "abcdon't()efgdon't()"
    assert find_sections(test_string) == [("", "abc"), ("don't()", "efg")]


EXAMPLE_STRING = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)


def test_find_does():
    assert find_dos(EXAMPLE_STRING) == [
        "xmul(2,4)&mul[3,7]!^",
        "?mul(8,5))",
    ]


def test_step2():
    does = find_dos(EXAMPLE_STRING)
    multiplications = [
        (a, b) for do_section in does for a, b in find_multiplications(do_section)
    ]

    assert multiplications == [(2, 4), (8, 5)]
