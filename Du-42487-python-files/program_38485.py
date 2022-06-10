#!/bin/usr/env python
import time

def countdown(num):
	if num > 0: 
		print(num) 
		time.sleep(0.1)
		num = num - 1
		countdown(num)
	else:
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

def index(str,letter,pos):
	if pos == len(str):
		return -1
	elif str[pos] == letter:
		return pos
	else:
		index(str,letter,pos+1)

if __name__ == '__main__':

	print(index('python','a',0))
	print(index('python','h',0))


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

