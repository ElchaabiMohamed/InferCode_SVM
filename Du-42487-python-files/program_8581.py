def swap_unique_keys_values(d):
	a = [v for k, v in list(d.items())]
	b = [c for c in a if a.count(c) == 1]
	return {v: k for k, v in list(d.items()) if v in b}









