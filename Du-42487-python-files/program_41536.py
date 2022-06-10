#!/usr/bin/env python

def swap(a,i,j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def reverse(a):
	i = 0
	while i < len(a):
		a[i] = a[len(a) - 1 - i]

def main():
	print(swap(a,2,3))
	print(reverse(a))

if __name__ == "__main__":
	main()