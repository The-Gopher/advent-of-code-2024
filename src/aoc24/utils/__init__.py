def nwise(iterable, window_size=2, min_item_count=2):
    x = [None] * (window_size - min_item_count) + iterable[:min_item_count]
    yield x
    for y in iterable[min_item_count:]:
        x = x[1:] + [y]
        yield x
    for _ in range(window_size - min_item_count):
        x = x[1:] + [None]
        yield x
