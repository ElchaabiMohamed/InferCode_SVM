def swap_keys_values(d):
	newd = {}
	for key in d:
		if d[key] in newd:
			del newd[d[key]]
		else:
			newd[d[key]] = key

	return newd