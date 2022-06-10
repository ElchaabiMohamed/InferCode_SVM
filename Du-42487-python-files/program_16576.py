import sys
def swap_keys_values(a):
    for (k,v) in a.items:
        tmp = k
        k = v
        v= tmp
    return sorted(a)