def swap_unique_keys_values(d):
	new = {}
	for key , value in list(d.items()):
		if value not in list(new.values()):
			new[key] = value

	for key , value in list(new.items()):
		d.pop(key, value)

	output = {}
	for key , value in list(new.items()):
		if value not in list(d.values()):
			output[key] = value

	inverse = {a: b for b, a in list(output.items())}
	return inverse