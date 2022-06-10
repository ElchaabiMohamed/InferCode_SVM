import time
def countdown(n):
 	while n > 0:
 		print(n)
 		n = n - 1
 		time.sleep(0.1)
 		if n == 0:
 			print("LIFT OFF!")

def search(string,letter):
	if letter not in string:
		return "False"
	else:
		return "True"

def index(str,letter):
	i = 0
	while i < len(str):
		if letter == str[i]:
			return i 
		i = i + 1
	return -1

def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		fibN_2 = 0
		fibN_1 = 1
		i = 2
		while i <= n:
			fibN = fibN_2 + fibN_1
			fibN_2 = fibN_1
			fibN_1 = fibN
			i = i + 1
		return fibN 