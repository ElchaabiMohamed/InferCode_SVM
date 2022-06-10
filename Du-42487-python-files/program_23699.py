def swap_keys_values(d):
    new = {}
    for k, v in list(d.items()):
        new[v] = k
    return new