import sys
def swap_unique_keys_values(a):
    value = list(a.values())
    keys = list(a.keys())        	
    dir = {}
    for i in range(0,len(vaules)):
        if value.count(value[i]) < 2:
            dir[value[i]] = keys[i]		
    return dir