
def swap_unique_keys_values(d):
	new_d = {}
	seen = []
	for key in d:
		seen.append(d[key])

	for key in d:
		if seen.count(d[key])==1:
			new_d[d[key]] = key
	return new_d
