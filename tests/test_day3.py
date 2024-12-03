from aoc24.day3.step1 import find_multiplications


def test_step1():
    string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert find_multiplications(string) == [(2, 4), (5, 5), (11, 8), (8, 5)]
