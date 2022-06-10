import time

def countdown(num):
	i = 0	
	while num > 0:
		print(num)
		num -= 1	
	print('LIFT OFF!')	
	

def search(ls,val):
	i = 0
	while i < len(ls):
		if ls[i] == val:
			return True
		i = i + 1
	return False

def index(str,letter):
	i = 0
	while i < len(str):
		if str[i] == letter:
			return i
		i = i + 1
	return '-1'

def fibonacci(n):
	first = 0
	second = 1
	while 0 < n:
		last = first
		first = second
		second = last + second
		n = n - 1
	return first




