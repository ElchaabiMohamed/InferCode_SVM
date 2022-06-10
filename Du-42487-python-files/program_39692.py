#!/usr/bin/env python

def swap(a,i,j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def reverse(a):
	i = 0
	while i < len(a) / 2:
		swap(a,a[i],a[len(a) - 1 - i])
		i += 1

def main():
	print(swap([1,2,3,4,5],2,3))
	print(reverse([1,2,3,4,5]))

if __name__ == "__main__":
	main()