def swap_unique_keys_values(d):
	a = {}
	dups = {}
	for k, v in list(d.items()):
		if v not in dups:
			if v in a:
				del a[v]
				dups[v] = True
			else:
				a[v] = k
	return a