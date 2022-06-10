#!/usr/bin/env python

a = [4, 3, 1, 2]

def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp
	return a

def reverse(a):
	i = 0
	while i < len(a) / 2:
		j = len(a) - i - 1
		swap(a, i, j)
		i = i + 1
	return a

def main():
   print(swap(a, 2, 3))
   print(reverse(a))

if __name__ == "__main__":
   main()