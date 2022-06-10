import sys

def swap_keys_values(d):
	keys = []
	vals = []
	new_d = {}
	for (k , v) in list(d.items()):
		keys.append(v)
		vals.append(k)
	y = 0
	for x in keys:
		new_d[x] = vals[y]
		y = y + 1
	return (new_d)


