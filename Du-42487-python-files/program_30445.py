def swap_keys_values(d):
    new_dict = dict((v, k) for k, v in list(d.items()))
    return new_dict
    #print(sorted(d.items(), key=lambda t: t[0]))