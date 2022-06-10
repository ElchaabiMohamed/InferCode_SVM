a = [4, 3, 1, 2]

def swap(a,i,j):
	while i < len(a)/2:
		tmp = a[i]
		a[i] = a[j]
		a[j] = tmp
		i = i + 1
		j = j - 1
	return a 

def reverse(a):
	i = 0
	j = len(a) - 1

def main():
	print(reverse.swap(a,2,3))

if __name__ == "__main__":
	main()
	