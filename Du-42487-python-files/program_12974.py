#!/usr/bin/env python

i = 1
while i < 101:
	if i%3 ==0:
		print('Fizz')
	elif i%5 == 0:
		'Buzz'
	elif i%5 == 0 and i%3 == 0:
		print('FizzBuzz')
	else:
		print(i)
	i = i + 1