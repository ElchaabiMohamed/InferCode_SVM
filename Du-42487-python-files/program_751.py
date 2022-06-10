#!/usr/bin/env python
def swap(a,n1,n2):
	tmp = a[n1]
	a[n1]=a[n2]
	a[n2]=tmp
	return a

def reverse(a):
	i = 0
	while i < len(a)/2:
		tmp = a[i]
		a[i] = a[len(a)-i-1]
		a[len(a)-i-1] = tmp
		i += 1
	return a
a = [4,3,1,2]
def main():
	print(swap(a,2,3))
	print(reverse(a))
if __name__ == '__main__':
	main()