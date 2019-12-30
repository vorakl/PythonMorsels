def deep_flatten(data):
    for item in data:
        if isinstance(item, str):
            yield item
        else:
            try:
                _ = iter(item)
            except TypeError:
                yield item
            else:
                yield from deep_flatten(item)
