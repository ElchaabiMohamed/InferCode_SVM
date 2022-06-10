def reverse_list(l):

	if len(l) == 0:
		new_l = list()
		return new_l
	
	new_l = reverse_list(l[1:])
	new_l.append(l[0])
	return new_l

def main():
	print((reverse_list([1,2,3])))
	print((reverse_list([3,4,5,6])))
	print((reverse_list([1,2])))
	
if __name__ == '__main__':
	main()