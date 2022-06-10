def swap_unique_keys_values(d):
    dictionary = {}
    unique = set(d.values())
    for (k, v) in list(d.items()):
        if v in unique:
            dictionary[v] = k
    return dictionary
