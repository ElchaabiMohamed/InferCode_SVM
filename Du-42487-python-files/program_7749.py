def swap_unique_keys_values(d):
    new = {}
    keys = [k for k in list(d.keys())]
    values = [v for v in list(d.values())]
    for k, v in list(d.items()):
        if values.count(v) == 1:
            new[v] = k
    return new