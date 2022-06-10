def swap_keys_values(d):
    d = dict((v,k) for k,v in list(d.items()))
    print((sorted(d.items())))
