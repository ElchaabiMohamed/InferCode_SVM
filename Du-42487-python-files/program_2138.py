def swap_keys_values(d):
	n_d = {}
	for k in d:
		n_d[d[k]] = k
	return n_d
