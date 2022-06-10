def countdown(num):
	import time
	if num == 0:
		print('LIFT OFF!')
	else:
		print(num)
		countdown(num-1)

def search(str,letter):
	if len(str) == 0:
		return False
	elif str[0] == letter:
		return True
	else:
		return search(str[1:],letter)

def index(str,letter,pos):
	if len(str) == 0:
		return -1
	elif str[pos] == letter:
		print(pos)
	else:
		return index(str,letter,pos+1)

def fibonacci(n):
	#fibonacci list created to n+1 position
	i = 0
	a = [0, 1]
	if n == 0:
		return a[len(a)]
	else:
		total = 0
		total = int(a[i]) + int(a[i+1])
		a.append(total)
		i = i + 1
		fibonacci(n-1)

