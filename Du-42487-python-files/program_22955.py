def swap_keys_values(d):
    new_dict = {}
    values_once = set(d.values())
    unique_values = []
    for n in values_once:
        if list(d.values()).count(n) == 1:
            unique_values.append(n)
    for k, v in list(d.items()):
        if v in unique_values:
            new_dict[v] = k
    return new_dict