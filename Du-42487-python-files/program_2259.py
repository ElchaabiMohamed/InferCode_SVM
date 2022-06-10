def swap_keys_values(d):
    new_dict = {}
    for keys in list(d.keys()):
        temp = d[keys]
        new_dict[temp] = keys
    return new_dict

