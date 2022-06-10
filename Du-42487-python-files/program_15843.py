def swap_keys_values(d):
    d = dict((v, k) for k, v in list(d.items()))
    #new_dict = sorted(d.items(), key=lambda t: t[0])
    print((sorted(list(d.items()), key=lambda t: t[0])))