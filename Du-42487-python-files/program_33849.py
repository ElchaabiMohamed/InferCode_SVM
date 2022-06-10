import sys
def swap_unique_keys_values(d):		
	store = {}
	val = []
	va = list(d.values())
	for i in va:
		val = va.append(i)
	for (k,v) in list(d.items()):	
		if va.count(v) == 1:
			store[k]=v
	return ({v:k for (k,v) in list(store.items())})


