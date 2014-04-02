def groupby(func, seq):
    grouped = {}
    for i in seq:
        if (func(i)) not in grouped:
            grouped[func(i)] = [i]
        else:
            (grouped[func(i)]).append(i)
    return grouped
