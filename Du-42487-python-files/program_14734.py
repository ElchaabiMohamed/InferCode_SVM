#!/usr/bin/env python
import sys

i = 1
while i <= 100:
	if i % 5 ==0 and i % 3 == 0:
		print("FizzBuzz")
	
	elif i % 3 == 0:
		print("Fizz")

	elif i % 5 == 0:
		print("Buzz")

	else:
		print(str(i))
	
	i = i + 1
