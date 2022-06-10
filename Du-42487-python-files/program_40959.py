def swap_keys_values(d):
    for(k, v) in list(d.items()):
        k,v = v,k
    return d