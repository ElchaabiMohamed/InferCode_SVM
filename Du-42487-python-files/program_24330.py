
def swap_keys_values(d):
    d2 ={}
    ds = sorted(d.items, reverse =True)
    for k,v in ds:
        d2[v] = k
    return d2
