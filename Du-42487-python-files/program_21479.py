#!/usr/bin/env python 

a = [2,4,5,0,2,6,3] 

def selection_sort(a):
	i = 0 
	while i < len(a):
		j = i + 1
		p = i 
		while j < len(a):
			if a[j] < a[p]:
				p = j 
			j = j + 1

		tmp = a[p]
		a[p] = a[i]
		a[i] = tmp

		i = i + 1

	return a

def main():
	print(selection_sort(a))

if __name__ == "__main__":
	main()