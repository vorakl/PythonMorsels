def window(iterable, wsize, *, fillvalue=None):
    if not wsize:
        return tuple()
    
    ii = iter(iterable)
    window = list()
    new_iter = True
    first_iter = True

    while True:
        while len(window) < wsize:
            try:
                item = next(ii)
            except StopIteration:
                if new_iter and not first_iter:
                    return
                else:
                    window.append(fillvalue)
            else:
                window.append(item)
            if new_iter:
                new_iter = False
            if first_iter:
                first_iter = False
        yield tuple(window)
        window[:] = window[1:]
        new_iter = True
