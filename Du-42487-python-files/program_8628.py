import sys

def swap_keys_values(d):
    keys = []
    values = []
    dic = {}

    for v, k in list(d.items()):
        keys.append(k)
        values.append(v)

    i = 0
    while i < len(values):
        dic[values[i]] = keys[i]
        i = i + 1

    return d