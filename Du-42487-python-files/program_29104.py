def swap_unique_keys_values(d):
    
    unique_values = list(set(d.values()))

    d = {v:k for k,v in list(d.items())}
    new_d = {}

    for key in unique_values:
        new_d[key] = d[key]
    return unique_values

