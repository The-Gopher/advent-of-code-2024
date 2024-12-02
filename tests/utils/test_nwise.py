def nwise(iterable, window_size=2, min_item_count=2):
    x = [None] * (window_size - min_item_count) + iterable[:min_item_count]
    yield x
    for y in iterable[min_item_count:]:
        x = x[1:] + [y]
        yield x
    for _ in range(window_size - min_item_count):
        x = x[1:] + [None]
        yield x


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
