#!/usr/bin/env python
def swap(p,i):
	tmp = a[p]
	a[p] = a[i]
	a[i] = tmp
	return a




def func_selection_sort(a):
	i = 0
	while i < len(a):
		p = i
		j = i + 1
		while j < len(a):
			if a[j] < a[p]:
				p = j
			j += 1

		swap(p,i)
		i += 1
	return a


def main():
	print(func_selection_sort(a))
if __name__ == '__main__':
	main()