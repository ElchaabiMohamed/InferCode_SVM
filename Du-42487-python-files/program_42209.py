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
	if len(str)-1 == pos:
		return -1
	elif str[pos] == letter:
		return pos
	else:
		return index(str,letter,pos+1)

a = [0,1]

def fibonacci(n):
	if n == len(a)-1:
		return a[n]
	elif n != len(a)-1:
		a.append(int(a[len(a)-1]+a[len(a)-2]))
	else:
		return fibonacci(n)

