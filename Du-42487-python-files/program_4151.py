def swap_unique_keys_values(d):
    a = [v for (k, v) in list(d.items())]
    for i in a:
        if a.count(i) == 1:
            a.pop(i)    
    e = {}
    for (k, v) in list(d.items()):
        if v not in a:
            e[v] = k
    return e

if "__name__" == "__main__":
    swap_unique_keys_values()
    
