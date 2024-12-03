from aoc24.utils import nwise


def test_nwise():
    assert list(nwise([1, 2, 3, 4, 5], 3, 3)) == [[1, 2, 3], [2, 3, 4], [3, 4, 5]]


def test_nwise_2():
    assert list(nwise([1, 2, 3, 4, 5], window_size=3, min_item_count=2)) == [
        [None, 1, 2],
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, None],
    ]
