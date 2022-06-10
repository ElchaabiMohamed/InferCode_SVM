#!/usr/bin/env python


x = eval(input())

if (x%3) == (x%5) ==0:
	print("fizz-buzz")
elif  (x%3)==0:
	print("fizz")
elif (x%5)==0:
	print("buzz")

else: 
	print(x)
