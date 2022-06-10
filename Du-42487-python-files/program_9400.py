def swap_unique_keys_values(d):
    n_dict = {}
    double = set()
    for k,v in list(d.items()):
        if v in n_dict:
            double.add(v)
        n_dict[v] = k
    for k in double:
        del n_dict[k]
    return n_dict

