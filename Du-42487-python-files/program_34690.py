import time

def countdown(num):
	if num == 0:
		print('LIFT OFF!')
	else:
		print(num)
		time.sleep(0.1)
		countdown(num - 1)

def search(ls,val):
	if ls == []:
		return False
	elif ls[0] == val:
		return True
	else:
		return search(ls[1:], val)

def index(str, letter, i):
	if i == len(str):
		return -1
	elif str[i] == letter:
		return i
	else:
		return index(str, letter, i + 1)

def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)
