d ={ "A": 4, "B": 3, "C":10, "D":10}

def swap_keys_values(d):
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

print((swap_keys_values(d)))
