import sys
def swap_keys_values(a):
    dir={}
    for i in a:
        dir[a[i]] = i 
    return sorted(dir)