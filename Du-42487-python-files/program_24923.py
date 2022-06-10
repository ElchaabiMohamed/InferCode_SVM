def swap_unique_keys_values(d):
    d=set(d)
    inv = {v: k for k, v in d}
    return inv