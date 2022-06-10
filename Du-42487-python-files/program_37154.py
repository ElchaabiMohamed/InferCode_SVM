def swap_unique_keys_values(d):
	seen = []
	new = {}
	for key, value in list(d.items()):
		if value not in seen:
			value.append(seen)
			new[key] = value
	inverse = {a: b for b, a in list(new.items())}
	return inverse