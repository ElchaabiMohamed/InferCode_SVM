def swap_unique_keys_values(d):
	dic = {}
	a = []
	b = []
	for key in d:
		value=d[key]
		if value not in a:
			a.append(value)
		else:
			b.append(value)
	for key in d:
		value = d[key]
		if value not in b:
			dic[value] = key
			a.append(value)
	return dic