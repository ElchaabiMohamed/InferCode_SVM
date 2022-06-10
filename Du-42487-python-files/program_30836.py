import sys

def swap_unique_keys_values(d):
	new_dict = {}
	counter = {}
	for v in list(d.values()):
		if v not in counter:
			counter[v] = 0
		counter[v] += 1

	for k, v in list(d.items()):
		if counter[v] < 2:
			new_dict[v] = k

	return new_dict