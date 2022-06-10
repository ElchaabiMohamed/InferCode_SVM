import sys
def swap_unique_keys_values(a):
    lis = []
    val = list(a.values())
    for no in val:
        print((lis(val)))
        if val.count(no) > 1:
            lis.append(no)			
    dir={}
    for i in a:
        if a[i] not in lis:
            dir[a[i]] = i 
    return dir