# import sys
def swap_keys_values(d):
	swp_d={}
	for lines in d:
		swp_d[(d[lines])]=lines
	return (swp_d)


# def main():
# 	my_dict = {'a' : 4, 'b' : 7, 'c' : 10}
# 	new_dict=swap_keys_values(my_dict)
# 	print(new_dict)
# if __name__ == '__main__':
# 	main()