import sys
def swap_unique_keys_values(d):		
	store = {}
	print((list(d.values())))
	for (k,v) in list(d.items()):
		print((d.count(v)))		
		if d.count(v) == 1:
			store[k]=v
	return ({v:k for (k,v) in list(store.items())})

