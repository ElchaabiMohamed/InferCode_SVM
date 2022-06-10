import sys

def swap_keys_values(my_dic):
	swapped_dic = {}
	dic_items = sorted(my_dic.items())
	for i in dic_items:
		key , value = i[0] , i[1]
		swapped_dic[value] = key

	return swapped_dic