import sys
def swap_unique_keys_values(d):		
	store = {}
	for key in d:
		for k in d:
			if d[key]  == d[k]:
				pass
			else:
				store[key] = d[key]
	return ({v:k for (k,v) in list(store.items())})


