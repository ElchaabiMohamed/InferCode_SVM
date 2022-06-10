def swap_unique_keys_values(d):
    d = {v:k for k,v in list(d.items())}
    new_d = {}
    for k in d:
        if k not in new_d:
            new_d[k] = d[k]
        else:
            del new_d[k]
            del d[k]
            del new_d[k]
    return new_d