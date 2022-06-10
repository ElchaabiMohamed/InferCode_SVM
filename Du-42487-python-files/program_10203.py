def swap_unique_keys_values(d):
    e = {}
    h = {}
    for k, v in sorted(list(d.items()), reverse=True):
    	if v not in e:
    		e[v] = k
    	else:
    		e[v] = 'n'
    for k, v in sorted(list(e.items()), reverse=True):
        if v != 'n':
           h[k] = v		
    return h


