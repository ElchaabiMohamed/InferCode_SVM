def swap_keys_values(d):
    newd = {}
    for key, value in list(d.items()):
        newd[value] = key
    return newd