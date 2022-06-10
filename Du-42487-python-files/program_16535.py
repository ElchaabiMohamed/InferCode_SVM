def swap(a,i,j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def reverse(a):
	i = 0
	while i < (len(a)/2):
		swap(a,i,len(a)-1-i)
		i += 1

a = [4, 3, 1, 2]
def main():
	func_reverse.swap(a,2,3)
	print(a)    # [4, 3, 2, 1]

	func_reverse.reverse(a)
	print(a)    # [1, 2, 3, 4]

	if __name__ == "__main__":
	   main()