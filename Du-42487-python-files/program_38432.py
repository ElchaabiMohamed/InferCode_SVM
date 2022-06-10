import sys
def swap_unique_keys_values(d):		
	store = {}
	di = d
	for key in d:
		for k in di:
			if di[k]  == d[key]:
				pass
			else:
				store[k] = d[k]
	return ({v:k for (k,v) in list(store.items())})


