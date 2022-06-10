def swap_unique_keys_values(d):
    if list(d.values()).count(d[k]) != 1 in list(d.keys()):
        del d[k]  
    inv = {v: k for k, v in list(d.items())}
    return inv