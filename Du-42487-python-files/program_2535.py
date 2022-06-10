def swap_unique_keys_values(d):
    new_d = {}
    dups = []
    for key, val in list(d.items()):
        if val not in dups:
            new_d[val] = key
            dups.append(val)
        else:
            del new_d[val]
    return new_d
