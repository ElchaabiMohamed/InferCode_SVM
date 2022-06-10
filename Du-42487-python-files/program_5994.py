def swap_keys_values(d):
    d2 = {}
    for k, v in list(d.items()):
        d2[v] = k
    return d2