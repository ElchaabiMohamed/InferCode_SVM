def swap_unique_keys_values(in_dict):
    out_dict = {}
    list = set()

    for k, v in in_dict.items:

        if v in out_dict():
            list.update([v])
            del out_dict[v]

        elif v not in list:
            out_dict[v] = k

    return out_dict