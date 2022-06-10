import sys
def swap_unique_keys_values(a):
    lis = []
    for no in a:
        lis.append(a[no])	
    dir = {}
    print(lis)
    for i in a:
        if no.count(lis) < 2:
            dir[a[i]] = i 
    return dir