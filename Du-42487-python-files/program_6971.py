#countdown
def countdown(n):
	import time

	if n ==1:
		print(n)
		time.sleep(0.1)
		print('LIFT OFF!')
	else:	
		print(n)
		time.sleep(0.1)
		countdown(n - 1)


#search
def search(str, letter):
	if str == '':
		return False
	elif str[0] == letter:
		return True
	else:
		return search(str[1:], letter)

#index
def index(str, letter,):
	i = 0
	while i < len(str):
		if str[i] == letter:
			return i
		i = i + 1
	return '-1'		
	

#fibonacci
def fibonacci(x):
	if x <= 1:
		return x
	else:
		return fibonacci(x - 1) + fibonacci(x-2)			
