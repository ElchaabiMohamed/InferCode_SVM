
def swap_unique_keys_values(d):
	lst = []
	for k in list(d.keys()):
		v = d[k]
		lst.append(v)
	new_d = {v:k for k, v in list(d.items()) if lst.count(v, 0, len(lst)) == 1}
	return new_d