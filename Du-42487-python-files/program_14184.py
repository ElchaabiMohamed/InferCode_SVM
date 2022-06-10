#!/bin/usr/env python
import time


def countdown(num):
	
	i = 0
	while num > i:
		print(num)
		time.sleep(0.1)
		num -= 1
	print('LIFT OFF!')

if __name__ == '__main__':

	print(countdown(3))
	print(countdown(5))

def search(str,letter):

	if letter in str:
		return True
	else:
		return False

if __name__ == '__main__':

	print(search('python','a'))
	print(search('python','h'))

def index(str,letter):

	start = len(str) - 1
	end = -1
	while start > end:
		if letter == str[start]:
			return start
		else:
			start -= 1
	return end

if __name__ == '__main__':

	print(index('python','a'))
	print(index('python','h'))

def fibonacci(n):

	a = 0
	b = 1
	for i in range(0, n):
		temp = a
		a = b
		b = temp + b
	return a

if __name__ == '__main__':

	print(fibonacci(3))
	print(fibonacci(6))


	


	
