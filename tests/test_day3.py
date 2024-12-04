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


def test_find_does_error1():
    test_string = ",what(936,615)*:who()[[[~:mul(364,505)~;&{-*mul(431,254))  select(){}#*+]mul(617,948)$mul(117,664){) &why()<,why()mul(271,823)what(674,989);/~{'+[mul(311,405),-!mul(651,968)$?;[from()+  {mul(595,193)*}]what()^mul(250,791)!mul(114,297))]$from()from(573,794)how()why()how()mul(130,657)how()select(){what()mul(676,119)>{~@{%why(105,423)mul(307,665)&mul(757,115)/'*{};:mul(800,484),[:(,+why()~mul(679,186)]#where()'~where() do()"

    sections = find_sections(test_string)
    assert len(sections) == 1
    assert len(find_dos(test_string)) == 1


def test_step2():
    does = find_dos(EXAMPLE_STRING)
    multiplications = [
        (a, b) for do_section in does for a, b in find_multiplications(do_section)
    ]

    assert multiplications == [(2, 4), (8, 5)]
