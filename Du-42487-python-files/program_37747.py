def swap_unique_keys_values(d):
    dictionary = {}
    unique = []
    for (k, v) in list(d.items()):
        unique.append((k, v))
    for (k, v) in unique:
        if unique.count(v) > 1:
            print(v)
