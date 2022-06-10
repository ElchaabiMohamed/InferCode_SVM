import sys
def swap_keys_values(a):
    for i in a:
        tmp = i
        i = a[i]
        a[i] = tmp
    return sorted(a)