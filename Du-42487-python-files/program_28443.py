def reverse_list(l):
	if len(l) == 1:
		return [l[0]]
	elif len(l) == 0:
		return []
	
	return reverse_list(l[1:]) + [l[0]]

def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))
    print((reverse_list([])))
    print((reverse_list([1])))
    print((reverse_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])))
    print((reverse_list([1,2,3,4,5,6,7,8])))

if __name__ == '__main__':
    main()