def reverse_list(x):
	if x == "":
		return x
	else:
		return x[-1] + reverse_list(x[:-1])


def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()