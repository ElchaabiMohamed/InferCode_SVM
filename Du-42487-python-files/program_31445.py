def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def reverse(a):
	i = 0
	while i < len(a)/2:
		swap(a, i, len(a)-1-i)
		i += 1

def main():
	a = [4, 3, 1, 2]
	reverse(a)
	print(a)
	swap(a, 0, 3)
	print(a)

if __name__ == "__main__":
	main()