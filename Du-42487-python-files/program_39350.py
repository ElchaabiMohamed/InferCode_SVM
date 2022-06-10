import sys
def swap_unique_keys_values(a):
    lis = []
    for no in a:
        lis.append(a[no])	
    dir = {}
    for i in a:
        if a[no].count(lis) < 2:
            dir[a[i]] = i 
    return dir