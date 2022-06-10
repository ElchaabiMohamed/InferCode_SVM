def swap_unique_keys_values(d):
    new = {}
    keys = [key for key in list(d.keys())]
    values = [value for value in list(d.values())]
    for v in list(d.values()):
        if values.count(v) == 1:
            new[v] = k
    return new