import time

def countdown(num):
	while num >= 1:
		print(num) 
		time.sleep(0.1)
		num = num + 1
	if num == 0:
		print("LIFT OFF!")

def search(str,letter):
	if letter in str:
		return "True"
	else:
		return "False"

def index(str,letter):
	if letter in str:
		return 1
	else:
		return -1

def fibonacci(n):
	if n > 1:
		return fibonacci(n-2) + fiboacci(n-1)
	return n 