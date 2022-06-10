def swap_keys_values(d):
    dic = {}
    keys = [key for key in list(d.keys())]
    values = [value for value in list(d.values())]
    for v in list(d.values()):
        if values.count(v) == 1:
            dic[v] = k
    return dic