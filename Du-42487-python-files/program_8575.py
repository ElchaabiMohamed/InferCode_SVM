# Swap keys with values but only unique values and ignore duplicates
def swap_unique_keys_values(d):
    # Have to explicitly convert dict_view type to list type in Python 3
    return dict([(v, k) for (k, v) in list(d.items()) if list(d.values()).count(v) == 1])
