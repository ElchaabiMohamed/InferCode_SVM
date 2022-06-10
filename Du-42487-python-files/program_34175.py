def swap_keys_values(d):
    dictionary = {}
    for (k, v) in list(d.items()):
        dictionary[v] = k
    return dictionary
