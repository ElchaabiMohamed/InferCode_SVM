import sys
def swap_keys_values(a):
    for (k,v) in list(a.items()):
        tmp = k
        k = v
        v = tmp
    print(a)
    return sorted(a)