def swap_unique_keys_values(d):
	new = {}
	for key , value in list(d.items()):
		if value not in list(new.values()):
			print(value)
			new[key] = value

	inverse = {a: b for b, a in list(new.items())}
	return inverse