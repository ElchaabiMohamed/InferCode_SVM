def swap_unique_keys_values(d):
    d=set(d)
    d={k:v for (k,v) in d}
    inv = {v: k for k, v in list(d.items())}
    return d