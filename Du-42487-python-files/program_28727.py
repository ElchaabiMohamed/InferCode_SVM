def swap_unique_keys_values(d):
    newd = {}
    for key, value in list(d.items()):
        if value not in newd:
            newd[value] = key
        else:
            del newd[value]
    return newd