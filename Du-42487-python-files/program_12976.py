def countdown(num):
	import time
	i = 0
	while i < int(num):
		print(int(num - i))
		time.sleep(0.1)
		i = i + 1

	print('LIFT OFF!')

def search(str,letter):
	if letter in str:
		return 'True'
	else:
		return 'False'

def index(str,letter):
	#while loop runs as long as the it doesnt come across the letter in the string
	#Also while i < length of the string and minus 1 as it starts with position 0
	i = 0
	while str[i] != letter and i < len(str)-1:
		i = i + 1

	if i+1 == len(str):
		return '-1'
	else:
		return i

def fibonacci(n):
	#fibonacci list created to n+1 position
	a = [0, 1]
	total = 0
	i = 0
	while i < n + 1:
		total = int(a[i]) + int(a[i+1])
		a.append(total)
		i = i + 1

	return a[n]