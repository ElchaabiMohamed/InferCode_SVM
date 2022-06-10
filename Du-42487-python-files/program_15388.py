
def swap_unique_keys_values(d):
    l = []
    new_d = {}
    for k in d:
        if d[k] not in l:
            new_d[d[k]] = k
            l.append(d[k])
    return new_d
        