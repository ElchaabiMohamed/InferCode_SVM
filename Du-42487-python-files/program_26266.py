def swap_unique_keys_values(dic):
	dic = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
	
	list_of_values=[dic[value] for value in dic]
	unique_dict = {}
	for key in dic:
		if list_of_values.count(dic[key]) == 1:
			unique_dict[dic[key]]=key
	return unique_dict