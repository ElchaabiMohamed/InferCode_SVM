from collections import Counter

def swap_unique_keys_values(s):
	new_dict = {}
	c = Counter(list(s.values()))
	l = [k for k, v in list(s.items()) if c[v] == 1]
	print(l)
	for key, value in list(s.items()):
		if key in l:
			new_dict[value] = key
	return new_dict