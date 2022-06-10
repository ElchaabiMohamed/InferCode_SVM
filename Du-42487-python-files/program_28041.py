def swap_keys_values(d):
    d = dict((v, k) for k, v in list(d.items()))
    sd = sorted(d.items())
    print(sd)

