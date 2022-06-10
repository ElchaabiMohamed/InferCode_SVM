def swap_keys_values(d):
    inv = {v: k for k, v in list(d.items())}
    return inv