def swap_unique_keys_values(d):
	a, b = [v for k, v in list(d.items())], [c for c in a if a.count(c) == 1]
	return {v: k for k, v in list(d.items()) if v in b}









