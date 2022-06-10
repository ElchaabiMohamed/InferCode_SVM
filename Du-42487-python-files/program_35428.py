def swap_unique_keys_values(d):
    d=list(set(d))
    inv = {v: k for k, v in list(d.items())}
    return d