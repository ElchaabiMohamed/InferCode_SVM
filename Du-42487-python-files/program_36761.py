a = [4, 3, 1, 2]

def reverse(a):
	j = 0
	i = len(a) - 1
	return j,i

def swap(a,i,j):
	while j < len(a)/2:
		tmp = a[j]
		a[j] = a[i]
		a[i] = tmp
		j = j + 1
		i = i - 1
	return a 


def main():
	print(reverse.swap(a,2,3))

if __name__ == "__main__":
	main()
	