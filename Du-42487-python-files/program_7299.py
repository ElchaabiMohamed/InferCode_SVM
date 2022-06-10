#!/usr/bin/env python
a = []

def swap(a,i,j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp
	return a

def reverse(a):
	i = 0
	while i<len(a):
		tmp = a[i]
		a[i] =  a[len(a) -i - 1]
		a[len(a) -i - 1]
		i = i + 1
	return a

def main():
	print(swap(a,2,3))
	print(reverse(a))

if __name__ == "__main__":
	main()