def swap_unique_keys_values(d):
	dictionary = {}
	unique = []
	for key in d:
		if not d[key] in unique:
			unique.append(key)
		dictionary[d[unique]] = key
	return dictionary