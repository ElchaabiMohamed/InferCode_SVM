def reverse_list(l):

	reversedlist = []

	i = len(l) - 1
	while i > -1:

		reversedlist.append(l[i])
		i = i - 1
	return reversedlist



def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()
