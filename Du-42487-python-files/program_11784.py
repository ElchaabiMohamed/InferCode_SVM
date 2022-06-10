def swap_keys_values(d):
    new_d = {val:key for (key, val) in list(d.items())}
    return(new_d)
