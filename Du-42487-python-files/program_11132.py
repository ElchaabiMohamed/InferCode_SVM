

def swap_unique_keys_values(d):
    keys = []
    values = []
    dic = {}

    for k, v in list(d.items()):
        keys.append(k)
        values.append(v)

    i = 0
    while i < len(values) and values[i] not in values:
        dic[values[i]] = keys[i]
        i = i + 1

    return dic