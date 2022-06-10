def swap_unique_keys_values(d):
    d = {v:k for k,v in list(d.items())}
    new_d = {}
    for (k,v) in d:
        if k not in new_d:
            new_d[k] = v
    return new_d