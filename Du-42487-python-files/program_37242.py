def swap_unique_keys_values(d):
	print(d)
	n_d = {}
	dup = []
	for k in d:
		if k in n_d:
			dup.append(k)
		n_d[d[k]] = k
	print(dup)
	for d in dup:
		n_d.pop(d)
	return n_d
