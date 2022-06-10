import sys
def swap_unique_keys_values(a):
    lis=[]
    for no in list(a.items()):
        if a.count(no) > 1:
            lis.append(no)            		
    dir={}
    for i in a:
        if dir[a[i]] not in lis:
            dir[a[i]] = i 
    return dir