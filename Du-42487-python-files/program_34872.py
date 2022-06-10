def swap_unique_keys_values(d):
    a = []
    b = []
    for key in list(d.keys()):
        a.append(key)
        b.append(d[key])
    d_new = {}
    for i in range(0,len(a)):
        if b.count(b[i]) == 1:
            d_new[b[i]] = a[i]
    return d_new