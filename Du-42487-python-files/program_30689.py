def swap(a,i,j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def reverse(a):
	i = 0
	tmp = ""
	while i < len(a)/2:
		tmp = a[i]
		a[i] = a[len(a)-i-1]
		a[len(a)-i-1] = tmp
		i += 1

def main():
	print(swap(hello, 2 ,4))
	print(reverse(hello))

if __name__ == "__main__":
	main()