#!/usr/bin/env python
def selection_sort(a):
	i = 0
	while i < len(a):
		j = i
		p = j + 1

		while p < len(a):
			if a[p] < a[j]:
				j = p
			p += 1
		tmp = a[j]
		a[j]= a[i]
		a[i]= tmp
		i += 1
	return a

def main():
	print(selection_sort(a))
if __name__ == '__main__':
	main()