import sys
def swap_unique_keys_values(a):
    lis = []
    for no in a:
        lis.append(str(a[no]))	
    dir = {}
    for i in a:
        if str(a[no]).count(lis) < 2:
            dir[a[i]] = i 
    return dir