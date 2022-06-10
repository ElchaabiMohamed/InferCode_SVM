def sumup(n):
	if n == 1:
		return 1
	n = n + sumup(n-1)
if __name__ == '__main__':
	main()