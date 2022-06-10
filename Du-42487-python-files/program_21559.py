def reverse_list(a):
	if a == []:
		return []
	temp = reverse_list(a[1:])
	temp.append(a[0])
	return temp

def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()

# [3, 2, 1]
# [6, 5, 4, 3]
# [2, 1]