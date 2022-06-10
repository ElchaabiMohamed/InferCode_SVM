def swap_keys_values(s):
	dic = {}
	for key, value in s.item():
		dic[value] = key
	return dic