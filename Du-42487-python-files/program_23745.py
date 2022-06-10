def swap_unique_keys_values(d):
    inv = {v: k for k, v in list(d.items())}
    for k in list(inv.keys()):
        if list(inv.keys()).count(inv[k]) > 1:
            del inv[k]  

    return inv