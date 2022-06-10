
def swap_unique_keys_values(d):
	new_d = {}
	seen = set()
	for key in d:
		seen += d[key]

	for key in d:
		if d[key] in seen:
			new_d[d[key]] = key
	return new_d
