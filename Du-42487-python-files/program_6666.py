def swap_unique_keys_values(d):
	l = []
	m = []
	for v in list(d.items()):
		if v in l:
			m.append(v)
		else:
			l.append(v)
	return {v: k for (k,v) in list(d.items()) if v not in m}
