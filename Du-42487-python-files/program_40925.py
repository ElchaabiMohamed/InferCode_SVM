import time

def countdown(num):
	i = 0
	while i < len(num): 
		return int(num) - 1
		i = i + 1


def search(str, letter):
	if letter in str:
		return "True"
	else:
		return "False"

def index(str, letter):
	if letter in str:
		return str.find(letter)
	else:
		return "-1"

def fibonacci(n):
	if n == 0: 
		return 0
	elif n == 1: 
		return 1
	else:
		return F(n-1)+F(n-2)
