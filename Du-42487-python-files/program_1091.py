a = [1, 3, 2, 4]

def swap(a, i, j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp
	return a

def reverse(a):
	i = 0
	while i < len(a)/2:
		swap(a, i, (len(a) - 1 -i) )
		i += 1
	return a

def main():
	print(swap(a, 0, 3))
	print(reverse(a))

if __name__ == "__main__":
	main()