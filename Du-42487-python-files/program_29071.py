def swap_unique_keys_values(d):
    dictionary = {}
    counter = []
    new = []
    for (k, v) in list(d.items()):
        counter.append(v)
    for c in counter:
        if counter.count(c) == 1:
            new.append(c)
    for (k, v) in list(d.items()):
        if v in new:
            dictionary[v] = k
    return dictionary
