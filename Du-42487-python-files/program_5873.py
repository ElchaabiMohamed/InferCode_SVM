a = [1, 2, 3, 1, 2, 3]

def swap(a,i,j):
 	tmp = a[j]
 	a[j] = a[i]
 	a[i] = tmp
 	return a

def selection_sort(a):
	i = 0
	while i < len(a):
		p = i
		j = i + 1

		while j < len(a):
			if a[j] < a[p]:
				p = j
			j = j + 1

		swap(a,i,p)
		i = i + 1

	return a

def main():
	print(selection_sort(a))

if __name__ == "__main__":
   main()