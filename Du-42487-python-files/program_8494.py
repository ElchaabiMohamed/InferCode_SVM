def swap_unique_keys_values(d):
	new = {}
	for key , value in list(d.items()):
		if value not in list(new.values()):
			new[key] = value
		else:
			del new[key]


	inverse = {a: b for b, a in list(new.items())}
	return inverse