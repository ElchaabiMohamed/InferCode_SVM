import sys
def swap_unique_keys_values(d):		
	store = {}
	va = list(d.values())
	print (va)
	for (k,v) in list(d.items()):	
		if va.count(v) == 1:
			store[k]=v
	return ({v:k for (k,v) in list(store.items())})


