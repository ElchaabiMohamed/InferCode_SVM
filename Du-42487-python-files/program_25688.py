def swap_keys_values(d):
    keys = []
    values = []
    for key in d:
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