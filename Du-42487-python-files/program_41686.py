

def swap_unique_keys_values(d):
	opposite = {}
	for k in d:
		if k not in opposite:
			opposite[d[k]] = k
		elif k in opposite:
			del opposite[k]	
	return opposite




