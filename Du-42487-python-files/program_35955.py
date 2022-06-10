def swap_unique_keys_values(d):
    return {a[1]: a[0] for a in list(d.items()) if list(d.values()).count(a[1]) == 1}