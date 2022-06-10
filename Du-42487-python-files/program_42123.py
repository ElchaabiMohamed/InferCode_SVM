#!/usr/bin/env python

def swap(a , i , j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def reverse(a):
	i = 0
	j = a[len(a - i - 1)]
	swap(a, 0, j)
	i = i + 1

def main():
	print(swap(a, 2, 3))
	print(reverse(a))

if __name__ == "__main__":
	main()