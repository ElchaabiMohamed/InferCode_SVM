a = [1, 2, 3, 1, 2, 3]

def swap(a,i,j):
	tmp = a[j]
	a[j] = a[i]
	a[i] = tmp

def lowest(a,i):
	p = i
	j = i + 1
	while j < len(a):
		if a[j] < a[p]:
			p = j
		j = j + 1
	return p

def selection_sort(a):
	i = 0
	while i < len(a):
		p = lowest(a,i)
		swap(a,i,p)
		i += 1

def main():
	selection_sort(a)
	print(a)

if __name__ == "__main__":
	main()