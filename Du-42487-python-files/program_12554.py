import sys

def swap_unique_keys_values(d):
	nd = {}
	for (i,v) in list(d.items()):
		if v not in nd:
			nd[v] = i
		elif v in nd:
			del nd[v]
			# del v



	return nd




def main():
	d = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
	print((swap_unique_keys_values(d)))
	# pass

if __name__ == '__main__':
	main()



# >>> import swap_v2_042 as swap
# >>> my_dict = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
# >>> new_dict = swap.swap_unique_keys_values(my_dict)
# >>> my_dict.items()
# dict_items([('a', 4), ('b', 7), ('c', 10), ('d', 7)])
# >>> new_dict.items()
# dict_items([(10, 'c'), (4, 'a')])

