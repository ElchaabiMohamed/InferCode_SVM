

def swap_unique_keys_values(d):
	opposite = {}
	for k in d:
		if k not in opposite:
			opposite[d[k]] = k
		else:
			del d[k]	
	return opposite




