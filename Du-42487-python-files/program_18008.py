def swap_unique_keys_values(d):
	dictionary = {}
	unique = []
	for key in d:
		if not d[key] in unique:
			unique.append(d[key])
		for i in unique:
			dictionary[unique[1]] = key
	return dictionary