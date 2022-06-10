def swap_keys_values(d):
    keys = list(d.keys())
    values = list(d.values())
    new = {}
    i = 0
    while i < len(keys):
        val = values[i]
        key = keys[i]
        new[val] = key
        i = i + 1
    return new