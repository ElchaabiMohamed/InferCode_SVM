def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def reverse(a):
	for i in range(len(a) / 2):
		swap(a, i, len(a)-i-1)

def main():
	a = [4, 3, 1, 2]

	swap(a, 2, 3)
	print(a)

	reverse(a)
	print(a)

if __name__ == '__main__':
	main()