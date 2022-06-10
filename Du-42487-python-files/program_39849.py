#!/usr/bin/env python
a = [1,2,3,4,5,6,7,8,9]

def reverse(a):
	i = 0
	while i < len(a)/2:
		tmp = a[i]
		a[i] = a[len(a)-i-1]
		a[len(a)-i-1] = tmp
		i += 1
	return a

def main():
	
	print(reverse(a)) 

if __name__ == '__main__':
	main()