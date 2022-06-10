def reverse_list(a):
	if len(a) == 0:
		return a
	e = a[0]
	a = a[1:]
	b = reverse_list(a) + [e]
	return b

def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()
