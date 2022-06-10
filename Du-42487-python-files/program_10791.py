def swap_unique_keys_values(d):
	n_d = {}
	dup = []
	for k in d:
		if d[k] in n_d:
			dup.append(d[k])
		n_d[d[k]] = k
	for x in dup:
		n_d.pop(x)
	return n_d
