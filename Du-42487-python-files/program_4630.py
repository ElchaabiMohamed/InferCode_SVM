import sys
def swap_unique_keys_values(d):		
	store= {}
	value= []
	va= list(d.values())
	for i in va:
		value.append(i)
	for (k,v) in list(d.items()):	
		if value.count(v)== 1:
			store[k]=v
	return ({v:k for (k,v) in list(store.items())})