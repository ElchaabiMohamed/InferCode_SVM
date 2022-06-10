import time

def countdown(num):
	if num == 0:
		print('LIFT OFF!')
	else:
		print(num)
		time.sleep(0.1)
		countdown(num - 1)

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
    else: return F(n-1)+F(n-2)
