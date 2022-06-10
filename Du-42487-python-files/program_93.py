import sys
def swap_unique_keys_values(d):		
	store = {}
	for (k,v) in list(d.items()):	
		if d.values.count(v) == 1:
			store[k]=v
	return ({v:k for (k,v) in list(store.items())})


