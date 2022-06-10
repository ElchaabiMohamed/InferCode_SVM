def swap_keys_values(d):
	new = {}
	keys = [k for k in list(d.keys())]
	values = [v for v in list(d.values())]
	for k, v in list(d.items()):
		if v not in new:
			new[v] = k
	return new

# d = {'a':4, 'b':7, 'c': 10, 'd':7}
# new = swap_keys_values(d)

# print (new.items())