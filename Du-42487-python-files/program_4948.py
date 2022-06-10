def swap_unique_keys_values(d):
    counter = {}
    for v in list(d.values()):
        counter[v] = counter.get(v,0) + 1
    unique = {k:v for k, v in list(d.items()) if counter[v] == 1}
    new_d = {val:key for (key, val) in list(unique.items())}
    return(new_d)
