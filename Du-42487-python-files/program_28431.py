#!usr/bin/env python
n = 1
while n <= 100:
	print(n)
	n = n + 1
	if n % 3 == 0:
		print('fizz')
	elif n % 5 == 0:
		print('buzz')
	elif n % 3 == 0 or n % 5 == 0:
		print('fizzbuzz')
