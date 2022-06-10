def swap_unique_keys_values(d):
    e = {}
    for s in d:
        if d[s] and s not in e:
           e[s] = d[s]
        print(d[s])

    return {v: k for k, v in list(e.items())}


