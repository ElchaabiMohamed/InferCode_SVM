def swap_unique_keys_values(d):
    v=list(d.values())
    for k in v:
        if v.count(v[k]) != 1:
            del d[k]  
    inv = {v: k for k, v in list(d.items())}
    return inv