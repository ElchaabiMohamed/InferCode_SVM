def swap_unique_keys_values(d):
    a = [v for (k, v) in list(d.items())]
    for i in a:
        if 1 < a.count(i):
            a = [j for j in a if j != i]    
    e = {}
    for (k, v) in list(d.items()):
        if v in a:
            e[v] = k
    return e

if "__name__" == "__main__":
    swap_unique_keys_values()
    
