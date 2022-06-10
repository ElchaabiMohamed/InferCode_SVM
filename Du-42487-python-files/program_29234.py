def swap_unique_keys_values(d):
    new_dict = dict((v, k) for k, v in list(d.items()))
    new_dict.pop(7, None)
    return new_dict
