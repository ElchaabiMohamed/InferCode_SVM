import sys
def swap_unique_keys_values(d):		
	store = {}
	di = d
	for key in d[0:-1]:
		for k in di[1:]:
			if d[key]  == di[k]:
				continue
			else:
				store[key] = d[key]
	return ({v:k for (k,v) in list(store.items())})


