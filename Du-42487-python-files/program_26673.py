def swap_unique_keys_values(d):
	swp_d={}
	nums=[]
	final_nums=[]
	dic={}
	for lines in d:
		nums.append(str(d[lines]))
		swp_d[(d[lines])]=lines
	for lines in nums:
		if nums.count(lines)==1:
			final_nums.append(int(lines))

	for words in final_nums:
		dic[words]=(swp_d[words])
	return (dic)


# def main():
# 	my_dict = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
# 	new_dict=swap_keys_values(my_dict)
# 	print(new_dict)
# if __name__ == '__main__':
# 	main()