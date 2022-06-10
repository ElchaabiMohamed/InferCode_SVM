import time

def countdown(t):
	while t > 0:
		print(t)
		time.sleep(0.1)
		t -= 1
	print("LIFT OFF!")
	
def search(s,l):
	contains = False
	for c in s:
		if c == l:
			contains = True
	return contains 	
	
def index(s,l):
	i, first = 0, -1
	while i < len(s):
		if s[i] == l:
			first = i
			break
		i += 1
	return first

def fibonacci(n):
	if n == 0:
		a = 1
	else:
		a,b = 1,1
		for i in range(n-1):
			a,b = b,a+b
	return a	
	
if __name__ == "__main__":
	countdown(3)
	print(search("hello", "o"))
	print(search("hello", "x"))
	print(index("hello", "o"))
	print(index("hello", "x"))
	print(fibonacci(3))
	print(fibonacci(6))
	print(fibonacci(0))
	