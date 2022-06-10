def swap_keys_values(dict_in):
    new_dict = {}
    for k,v in list(dict_in.items()):
        new_dict[v] = k

    return new_dict