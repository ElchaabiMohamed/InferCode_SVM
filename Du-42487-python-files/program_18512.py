import sys
def swap_unique_keys_values(a):
    lis = ''
    for no in a:
        lis += a[no] 	
    dir = {}
    for i in a:
        if lis.count(str(a[no])) < 2:
            dir[a[i]] = i 
    return dir