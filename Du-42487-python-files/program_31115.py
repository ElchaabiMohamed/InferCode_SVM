def swap_unique_keys_values(d):
    for k in list(d.keys()):
        if list(d.values()).count(d[k]) > 1:
            del d[k]  
    inv = {v: k for k, v in list(d.items())}
    return inv