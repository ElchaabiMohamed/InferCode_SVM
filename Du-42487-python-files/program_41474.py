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
