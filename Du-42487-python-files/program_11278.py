def swap_unique_keys_values(d):
    seen = {} 
    result = {} 
    for k,v in list(d.items()):
        if v in seen:
            del seen[v]
        else:
            seen[v] = k
            result[v] = k
    return seen