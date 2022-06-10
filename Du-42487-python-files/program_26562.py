import sys


def swap_unique_keys_values(d):
    a2 = {}
    a3 = {}
    ar = sorted(list(d.items()), reverse = True)
    for k,v in ar:
        if v not in a2:
          a2[v] = k
        else:
          a2[v] = "N"
    ar2 = sorted(list(a2.items()), reverse = True)
    for k,v in ar2:
      if v != "N":
        a3[k] = v
    return a3