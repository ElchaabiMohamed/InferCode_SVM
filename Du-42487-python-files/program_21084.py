def swap_unique_keys_values(d):
    e = {}
    h = {}
    for k, v in sorted(list(d.items()), reverse=True):
    	if v in e:
    		e[k] = v
    	else:
    		e[k] = 'n'
    for k, v in sorted(list(e.items()), reverse=True):
        if v != 'n':
           h[k] = v		
           
    
    

    return {v: k for k, v in list(d.items())}


