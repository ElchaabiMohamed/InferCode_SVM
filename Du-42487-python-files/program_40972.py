def swap_unique_keys_values(d):
	count = {}
	for v in [v for k, v in list(d.items())]:
		if v not in count:
			count[v] = 1
		else:
			count[v] += 1

	multiples = [k for k, v in list(count.items()) if v > 1]
	new_d = {}
	for k, v in list(d.items()):
		if v not in multiples:
			new_d[v] = k
	return new_d