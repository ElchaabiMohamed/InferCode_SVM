def swap_unique_keys_values(d):
    values = list(d.values())
    return {v : k for k, v in list(d.items()) if values.count(v) == 1}