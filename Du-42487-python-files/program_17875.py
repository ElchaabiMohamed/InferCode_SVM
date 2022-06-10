import sys
def swap_unique_keys_values(a):
    lis = []
    for no in a:
        lis.append(no)	
    dir = {}
    for i in a:
        if no.count(lis) > 1:
            dir[a[i]] = i 
    return dir