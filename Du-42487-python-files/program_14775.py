import time

def countdown(num):
	if num == 0:
		print("LIFT OFF!")
	else:
		print(num)
		countdown(num-1)
if __name__ == "__main__":
	print(num) 


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
	if n == 1:
		return 1
	elif n == 0:
		return 0
	else:
		return fibonacci(n-1) + fibonacci(n-2)
