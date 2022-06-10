def swap_unique_keys_values(d):
    e = {}
    for s in d:
        if d[s] not in e:
           e[s] = d[s]
        elif d[s] in e:
        	del d[s] 
    print (e)

    return {v: k for k, v in list(e.items())}


