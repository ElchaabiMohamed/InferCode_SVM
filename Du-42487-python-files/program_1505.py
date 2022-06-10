import sys

def swap_keys_values():
	keys = []
	values = []
	newd = {}
	for word in d:
		keys.append(word)
	for word in d:
		values.append(d[word])
	for i in range(0, len(values)):
		newd[values[i]] = keys[i]
	return newd
