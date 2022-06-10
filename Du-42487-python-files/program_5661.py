def swap_keys_values(d):
    new_dict = {v:k for k, v in list(d.items())}
    return new_dict