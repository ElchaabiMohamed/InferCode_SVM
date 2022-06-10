def swap_unique_keys_values(d):
    inv = {v: k for k, v in list(d.items())}
    d=[]
    for k in list(inv.keys()):
        d.append(k)
    for k in d:
        if d.count(k) > 1:
            del inv[k]
            del inv[k]

    return inv