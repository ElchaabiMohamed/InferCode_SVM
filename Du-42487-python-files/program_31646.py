import time

def countdown(num):
	while num >= 1:
		print(num)
		time.sleep(.1)
		num = num - 1
	if num == 0:
		print("LIFT OFF!")

def search(str,letter):
	i = 0
	while i < len(str):
		if letter in str:
			return True
		else:
			return False
		i = i + 1

def index(str,letter):
	if letter in str:
		return str.find(letter)
	else:
		return -1

def fibonacci(n):
	if n == 0:
		return 0
	else:
		return fibonacci(n-2) + fibonacci(n-1)
