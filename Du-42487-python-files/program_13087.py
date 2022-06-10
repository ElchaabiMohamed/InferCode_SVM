import sys

# def swap_keys_values(d):
# 	nd = {}
# 	for k,v in d.items():
# 		nd[v] = k

# 	return nd

def swap_unique_keys_values(d):
	nd = {}
	to_delete = []
	for k, v in list(d.items()):
		if v in nd:
			to_delete.append(v)
		else:
			nd[v] = k

	for k in to_delete:
		del nd[k]

	return nd

# def main():
# 	d = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
# 	print(swap_unique_keys_values(d))
# 	new_dict = swap_keys_values(my_dict)
# 	print(new_dict)
# 	 a = []
# 	 for k,v in d.items():
# 	 	a.append('{} {}'.format(k,v))

#  a_set = set(a)
#  b = a[:]
#  b_set = set(b)

#  inter = b_set.intersection(a_set)

# 	 for w in a:


# if __name__ == '__main__':
# 	main()
