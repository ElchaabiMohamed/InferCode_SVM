def swap_unique_keys_values(d):
    return {v: k for k ,v in list(d.items()) if d.values.count(k) > 1 }