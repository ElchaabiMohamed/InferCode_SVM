def swap_unique_keys_values(d):
    q = {}
    a = []
    b = []
    for key in d:
        value = d[key]
        if value not in a:
            a.append(value)
        else:
            b.append(value)
    for key in d:
        value = d[key]
        if value not in b:
            q[value] = key
            a.append(value)
    return q