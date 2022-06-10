import time

def countdown(n):
	while n > 0:
		print(n)
		time.sleep(0.1)	
		n = n - 1
		if n == 0:
			print("LIFT OFF!")
def search(string,letter):
	if letter not in string:
		return "False"
	else:
		return "True"
def index(string,letter):
	if letter not in string:
		return "-1"
	if letter in string:
      		a = list(string)
      		return a.index(letter)

def fibonacci(n):
	previous = 0
	current = 1
	i = 1
	if n < 1:
		return 0
	while i < n:
		temp = current
		current += previous
		previous = temp
		i = i + 1
	return current



#print fibonacci(0)
#print fibonacci(1)
#print fibonacci(6)




