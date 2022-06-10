import sys

def swap_unique_keys_values(my_dic):
	unique_dic = {}
	for k,v in list(my_dic.items()):
		if v in unique_dic:
			del unique_dic[v]
		else:
			unique_dic[v] = k

	return unique_dic