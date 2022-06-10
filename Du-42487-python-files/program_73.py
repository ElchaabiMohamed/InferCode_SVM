

def swap_unique_keys_values(d):
	unique = []
	for k in d:
		if d[k] not in unique:
			unique.append(d[k])
		elif d[k] in unique:
			unique.remove(d[k])
	opposite = {}
	for k in d:
		if k in unique:
			opposite[d[k]] = k
	return opposite




