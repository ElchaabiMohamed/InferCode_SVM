def swap_keys_values(d):
    new_d = {}
    for key, val in d:
        new_d[val] = key
    return new_d
