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

def index(str,letter,occurence):
	if occurence == len(str):
		return -1
	elif str[occurence] == letter:
		return occurence
	else:
		return index(str, letter, occurence + 1)

def fibonacci(n):
	if (n == 0):
		return 0
	elif (n == 1):
		return 1
	elif (n > 1):
		return(fibonacci(n-1) + fibonacci(n-2))
	else:
		return -1