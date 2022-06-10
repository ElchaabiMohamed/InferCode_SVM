def swap_unique_keys_values(d):
    keys = []
    values = []
    for key in d:
        values.append(d[key])
    for key in d:
        if d.count(values) == 1:
            keys.append(key)
            values.append(d[key])
    new = {}
    i = 0
    while i < len(keys):
        val = values[i]
        key = keys[i]
        new[val] = key
        i = i + 1
    return new