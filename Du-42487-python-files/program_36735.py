def swap_keys_values(d):
    e = {}
    for (k, v) in list(d.items()):
        e[v] = k
    return e

if "__name__" == "__main__":
    swap_keys_values()
    
