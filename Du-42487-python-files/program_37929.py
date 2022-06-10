#!/usr/bin/env python 

def swap(a, i, j):
	tmp = a[i]
	a[j] = a[i]
	a[i] = tmp

def reverse(a):
	i = 0
	while i < len(a) / 2:
		tmp = a[i]
		a[j] = a[i]
		a[i] = tmp
		j = j + 1
		i = i - 1


def main():
	print(swap(a, 3, 4))
	print(reverse(a))

if __name__ == "__main":
	main()