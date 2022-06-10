import sys

def swap_keys_values(d):
	# d = list(d)
	# d = d[::-1]
	nd = {}
	for (i,v) in list(d.items()):
		nd[v] = i
		# print(i, v)

	return nd

def main():
	d = {'a' : 4, 'b' : 7, 'c' : 10}
	print((swap_keys_values(d)))



if __name__ == '__main__':
	main()

# >>> import swap_v1_042 as swap
# >>> my_dict = {'a' : 4, 'b' : 7, 'c' : 10}
# >>> new_dict = swap.swap_keys_values(my_dict)
# >>> my_dict.items()
# dict_items([('a', 4), ('b', 7), ('c', 10)])
# >>> new_dict.items()
# dict_items([(10, 'c'), (4, 'a'), (7, 'b')])
# >>> my_dict['a']
# 4
# >>> new_dict[4]
# 'a'
