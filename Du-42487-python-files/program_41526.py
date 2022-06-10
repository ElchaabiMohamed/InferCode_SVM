def swap_keys_values(my_dict):
    new = {}
    for k,v in list(my_dict.items()):
        new[v] = k
    return new
