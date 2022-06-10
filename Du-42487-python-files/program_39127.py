#!usr/bin/env python

def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def smallest_element(a, i):
	p = i 
	j = i + 1
	while j < len(a):
		if a[p] < a[j]:
			j = p
		j = j + 1

	return p

def selection_sort(a):
	i = 0
	while i < len(a):
		p = smallest_element(a,i)
		swap(a, i, p)
		i = i + 1

def main():
	print(selection_sort(a))

if __name__ == "__main__":
	main()