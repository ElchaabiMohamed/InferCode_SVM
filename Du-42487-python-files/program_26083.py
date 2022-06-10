import sys

def swap_unique_keys_values(d):
    new = {}
    for k in d:
        v = d.get(k)
        if v in new:
            del new[v]
        else:
            new[v] = k
    return (new)
