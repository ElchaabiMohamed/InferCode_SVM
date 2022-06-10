import sys


def swap_keys_values(d):
    a2 = {}
    a3 = {}
    ar = sorted(list(d.items()), reverse = True)
    for k,v in ar:
      a2[v] = k
    ar2 = sorted(list(a2.items()), reverse = True)
    for k,v in ar2:
        a3[k] = v
    return a3