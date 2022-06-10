

def swap_unique_keys_values(d):
    keys = []
    values = []
    dic = {}

    for k, v in list(d.items()):
        keys.append(k)
        values.append(v)

    i = 0
    while i < len(values):
        j = 0
        while j < len(values):
            if values[i] == values[j] and i != j:
                pass

            else:
                new_values.append(values[i])

            j = j + 1
        i = i + 1

    i = 0
    while i < len(values):
        dic[values[i]] = keys[i]
        i = i + 1

    return dic