def swap_unique_keys_values(d):
    e = {}
    for s in d:
       
        
        if d[s] in d:
        	d.remove(s) 
    print (d)

    return {v: k for k, v in list(d.items())}


