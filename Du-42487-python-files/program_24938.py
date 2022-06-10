def swap_unique_keys_values(d):
	dictionary = {}
	unique = []
	for key in d:
		if not key in unique:
			unique.append(d[key])

	for key in unique:
		dictionary[d[key]] = key

	return dictionary