def swap_unique_keys_values(dic):
	unique_dict = {}
	for key in dic:
		if list(dic.values()).count(dic[key]) == 1:
			unique_dict[dic[key]] = key

	return unique_dict