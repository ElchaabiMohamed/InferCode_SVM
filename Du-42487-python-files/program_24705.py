def reverse_list(l):
	if len(l) == 0:
		return l
	return reverse_list(l[1:]) +[l[0]]


	#1,2,3
	#2,3         1
	#3			 2
	#[]			 3

def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()
