def swap_keys_values(d):
    dvalues = [v for v in list(d.values())]
    return {v : k for k, v in list(d.items()) if dvalues.count(v) < 2}