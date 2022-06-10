import time

def countdown(num):
	i = 0	
	while num > 1:
		print(num)
		num += num - 1	
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
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)

