def sorter(t):
    return t[1]


def swap_keys_values(d):
    d = dict((v,k) for k,v in list(d.items()))
    print((sorted(list(d.items()), key=sorter)))

