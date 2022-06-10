def swap_unique_keys_values(d):
    a = [v for v in list(d.values())]
    a = [v for v in a if a.count(v) == 1]
    return {v:k for k,v in list(d.items()) if v in a}
