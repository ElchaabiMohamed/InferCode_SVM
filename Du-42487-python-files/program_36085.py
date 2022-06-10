def reverse_list(a):
	if a == []:
		return []
	tmp = reverse_list(a[1:])
	tmp.append(a[0])
	return tmp



def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()