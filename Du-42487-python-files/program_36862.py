#!usr/bin/env python
n = 1
while 100 <= n:
	print(n)
	n = n + 1
	if n % 3 == 0:
		print('fizz')
	elif n % 5 == 0:
		print('buzz')
	elif n % 3 == 0 and n % 5 == 0:
		print('fizz buzz')