
def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp
	return a


def reverse(a):
	i = 0
	while i < len(a)/2:
		swap(a, i, len(a) - i - 1)
		i = i + 1
	return a 


def main():
	print(reverse([9, 8, 7, 6, 5, 4, 3, 2, 1]))

if __name__ == "__main__":
	main()


