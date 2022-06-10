a = [1,2,3,1,2,3]

def swap(a,i,j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def smallest(a,i):
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
		p = smallest(a,i)
		swap(a,i,p)
		i = i + 1

def main():
	print(selection_sort(a))

if __name__ == "__main__":
	main()
	