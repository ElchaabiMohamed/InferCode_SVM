#!/usr/bin/env 

def swap(a,i,j):
	tmp = a[j]
	a[j] = a[i]
	a[i] = tmp 	


def reverse(a):
	i = 0
	j = len(a)
	if j % 2 == 0:
		while i < (len(a)/2):
			tmp = a[j]
			a[j] = a[i]
			a[i] = tmp
			i = i + 1
			j = j - 1 	
	else:
		while i < ((len(a)/2) + 1):
			tmp = a[j]
			a[j] = a[i]
			a[i] = tmp
			i = i + 1
			j = j - 1

def main():
   print(double(5))
   print(double("Hello"))

if __name__ == "__main__":
   main()