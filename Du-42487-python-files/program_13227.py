def countdown(num):
	if num == 0:
		print("LIFT OFF!")
	else:
		print(num)
		countdown(num -1)

def search(str,letter):
	if letter in str:
		return "True"
	else:
		return "False"

def index(str):
	if letter in str[i]:
		return i
	else:
		return "-1"

def fibonacci(n):
	if (n == 0):
		return 0
	elif (n == 1):
		return 1
	elif (n > 1):
		return(fibonacci(n-1) + fibonacci(n-2))
	else:
		return -1