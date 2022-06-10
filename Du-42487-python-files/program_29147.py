def swap_unique_keys_values(d):
    new = {}
    for k, v in list(d.items()):
        if v not in new:
            new[v] = k
        else:
            del new[v]
    return new