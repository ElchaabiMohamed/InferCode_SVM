def swap_unique_keys_values(d):
	output = {}
	new = d
	for key , value in list(new.items()):
		new.pop(key, value)
		if value not in list(new.values()):
			output[key] = value



	inverse = {a: b for b, a in list(output.items())}
	return inverse