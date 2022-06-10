import sys

def swap_unique_keys_values(my_dict):
	
	dic = {}

	for key, value in list(my_dict.items()):
		if value in dic:
			del dic[value]
		else:
			dic[value] = key

	return dic