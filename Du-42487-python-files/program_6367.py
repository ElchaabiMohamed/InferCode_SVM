def sorter(t):
    return t[1]


def swap_keys_values(d):
    d = dict((v, k) for k, v in list(d.items()))
    print([(k,v) for (k, v) in sorted(list(d.items()), key=lambda x: x[1])])

