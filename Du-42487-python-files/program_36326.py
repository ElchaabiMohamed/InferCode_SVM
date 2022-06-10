def reverse_list(list):
	i = 0
	while i < len(list)//2:
		list[i], list[len(list)-1-i] = list[len(list)-1-i], list[i]
		i += 1
	return list

def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()