def swap_unique_keys_values(d):
    q = {}
    a = []
    for key in d:
        value = d[key]
        if value not in a:
        	q[value] = key
        	a.append(value)
    print(a)
    return q