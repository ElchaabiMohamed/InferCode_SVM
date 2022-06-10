a = [4 , 3, 1, 2]
i = 2
j = 3
def swap(a,i,j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp
	return a

def reverse(a):
	i = 0
	while i < len(a) / 2:
		swap(a, i, len(a) - 1 - i)
		i = i + 1
	return a


def main():
	print(swap(a, i, j))
	print(reverse(a))

if __name__ == "__main__":
	main()