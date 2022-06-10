def swap_keys_values(d):
    e = {}
    for (k, v) in d:
        e[v] = k
    return e

if "__name__" == "__main__":
    swap_keys_values()
    
