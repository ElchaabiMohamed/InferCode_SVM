#!/usr/bin/env python
a = [1,2,3,4,5,6,7,8,9]
def swap(a,i,j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp
	return a
def reverse(a):
	x = a[:: -1]
	return x

def main():
	print(swap(a,2,5))
	print(reverse(a)) 

if __name__ == '__main__':
	main()