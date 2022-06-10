import sys

def reverse_list(l):
	if l == []:
		return []
	elif len(l) == 1:
		return l	
	else:
		return reverse_list(l[-1:]).append(l[0])

def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()		