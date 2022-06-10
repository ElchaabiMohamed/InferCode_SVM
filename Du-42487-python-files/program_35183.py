def swap_keys_values(d):
    d = dict((v,k) for k,v in list(d.items()))
    print((list(d.items())))
