import sys

def reverse_list(l):
	new_l = []
	sortedl = [i for i in sorted[l]]
	for i in range(len(l)):
		new_l += sortedl[len(l)-i-1]
	return new_l

def main():
    print((reverse_list([1,2,3])))
    print((reverse_list([3,4,5,6])))
    print((reverse_list([1,2])))

if __name__ == '__main__':
    main()
