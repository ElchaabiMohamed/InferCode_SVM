def swap_unique_keys_values(d):
	dictionary = {}
	unique = []
	for key in d:
		if not key in unique:
			unique.append(key)

	for keys in unique:
		dictionary[d[keys]] = keys

	return dictionary