import sys
def swap_unique_keys_values(a):
    lis=[]
    for no in list(a.items()):
        print((no.count(a)))
        if no.count(a) > 1:
            lis.append(no)			
    dir={}
    for i in a:
        if a[i] not in lis:
            dir[a[i]] = i 
    return dir