def swap_keys_values(d):
    q = {}
    for key in d:
        value = d[key]
        q[value] = key
    return q