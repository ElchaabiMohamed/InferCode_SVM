def swap_unique_keys_values(d):
    dictionary = {}
    unique = []
    deli = []
    for (k, v) in list(d.items()):
        unique.append(v)
    for v in unique:
        if unique.count(v) > 1:
            deli.append(v)
    for v in unique:
        if v in deli:
            del unique[v]
    for (k, v) in list(d.items()):
        if v in unique:
            dictionary[v] = k
    return dictionary
