import time

def countdown(t):
	if t == 0:
		return 'LIFT OFF!'
	else:
		print(t)
		return countdown(t-1)
	return 'LIFT OFF'
		
def search(s,l, i=0):
	if i < len(s):
		if s[i] == l:
			contains = True
			return contains
		else:
			contains = False
			return search(s, l, i+1)
	else:
		return False
 	
def index(s,l, i=0):
	if i < len(s):
		if s[i] == l:
			contains = i
			return contains
		else:
			contains = -1
			return index(s, l, i+1)
	else:
		return -1

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
			
	
if __name__ == "__main__":
	print(countdown(5))
	print(search("hello", "o"))
	print(search("hello", "x"))
	print(index("hello", "o"))
	print(index("hello", "x"))
	print(fibonacci(3))
	print(fibonacci(6))
	print(fibonacci(0))