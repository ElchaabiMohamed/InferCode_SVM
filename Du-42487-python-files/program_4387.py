def swap_unique_keys_values(d):
    #from collections import Counter
    #v=list(d.values())
    #for k in v:
    #    if v.count(v[k]) > 1:
    #        del d[k]  
    inv = {v: k for k, v in list(d.items()) if v.count() == 1}
    return inv