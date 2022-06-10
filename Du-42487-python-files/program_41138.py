def swap_unique_keys_values(d):
	vals = list(d.values())
	return {v: k for k, v in list(d.items()) if vals.count(v) == 1}
