def swap_unique_keys_values(d):
    
    

    d = {v:k for k,v in list(d.items())}
    new_d = {}
    unique_values = list(set(d.values()))
    for key in unique_values:
        new_d[key] = d[key]
    return new_d

