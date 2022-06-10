def swap_unique_keys_values(d):
	val = list(d.values())
	for char in val:
		if char.count() > 1:
			del(val[char])

	dic = {}
	for key in d:
		value = d[key]
		dic[value] = key
	new_dic = {}
