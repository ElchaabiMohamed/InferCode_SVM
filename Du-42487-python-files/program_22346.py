def swap_unique_keys_values(d):
	dictionary = {}
	unique = []
	not_unique = []
	value = []
	for key in d:
		if not key in unique:
			unique.append(d[key])
		else:
			not_unique.append(d[key])
	for i in unique:
		if not not_unique in unique:
			value.append(i)
	for keys in value:
		dictionary[d[keys]] = keys

	return dictionary