def swap_unique_keys_values(d):
	dictionary = {}
	unique = []
	not_unique = []
	for key in d:
		if not key in unique:
			unique.append(key)
		else:
			not unique.append(key)

	for keys in unique:
		if not keys in unique:
			dictionary[d[keys]] = keys

	return dictionary