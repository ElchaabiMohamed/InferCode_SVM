def swap_keys_values(d):
    new_d = {}
    for key, val in list(d.items()):
        new_d[val] = key
    return new_d
