def swap_keys_values(d):
	final = {}
	for key in d:
		final[d[key]] = key
		
	return final