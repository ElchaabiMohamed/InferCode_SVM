def swap_unique_keys_values(d):
	new = {}
	for key , value in list(d.items()):
		d.pop(key, value)

		if value not in list(d.values()):
			new[key] = value



	inverse = {a: b for b, a in list(new.items())}
	return inverse