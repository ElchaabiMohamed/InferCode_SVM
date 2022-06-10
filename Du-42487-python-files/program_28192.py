#!/usr/bin/env python


i = 1 
while i <= 100:
	if (x%3) == (x%5) ==0:
		print("fizz-buzz")
	elif  (x%3)==0:
		print("fizz")
	elif (x%5)==0:
		print("buzz")
	else: 
		print(i) 
	i = i + 1
