
def swap_keys_values(in_dict):
    out_dict = {}
    for t,v in list(in_dict.items()):
        out_dict[v] = t

    return out_dict