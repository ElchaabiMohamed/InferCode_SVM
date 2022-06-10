def swap_keys_values(d):
    new_dict = {}
    for keys in list(d.keys()):
        temp = d[keys]
        if temp in new_dict:
            del new_dict[temp]
        else:
            new_dict[temp] = keys
    return new_dict
