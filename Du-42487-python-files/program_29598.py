import sys

def swap_unique_keys_values(d):
	seen = {}
	new_d = {}
	for k in d:
		seen[k] += 1
	for item in seen:
		if d[item] == 1:
			new_d[item] = True
	for k in new_d:
		for key in d:
			if k in d:
				new_d[k] = d[key]
	return new_d
