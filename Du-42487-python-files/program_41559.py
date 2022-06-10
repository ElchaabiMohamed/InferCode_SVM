# Simply swap keys with values
def swap_keys_values(d):
    return dict([(v, k) for (k, v) in list(d.items())])
