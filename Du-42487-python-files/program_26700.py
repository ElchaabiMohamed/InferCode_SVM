import sys
def swap_unique_keys_values(a):
    lis=[]
    for no in list(a.items()):
        if no.count(a) > 1:
            lis.append(no)            		
    dir={}
    for i in a:
        k = dir[a[i]]
        if k not in lis:
            dir[a[i]] = i 
    return dir