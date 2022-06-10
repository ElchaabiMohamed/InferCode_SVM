#!/usr/bin/env 

def swap(a,i,j):
	tmp = a[j]
	a[j] = a[i]
	a[i] = tmp 	


def reverse(a):
	i = 0
	j = len(a)
	if len(a) == 1:
		return a
	else:
		while i < len(a):
			tmp = a[j - i -1]
			a[j - i - 1] = a[i]
			a[i] = tmp
			i = i + 1 		

def main():
   print(double(5))
   print(double("Hello"))

if __name__ == "__main__":
   main()