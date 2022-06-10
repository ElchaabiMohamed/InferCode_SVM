import sys
def swap_unique_keys_values(d):		
	store = {}
	val = []
	va = list(d.values())
	for i in va:
		val.append(i)
	print (val)
	for (k,v) in list(d.items()):	
		if val.count(v) == 1:
			store[k]=v
	return ({v:k for (k,v) in list(store.items())})


