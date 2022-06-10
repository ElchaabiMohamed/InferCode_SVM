import time
def countdown(num):
	if num == 1:
		print(num)
		print("LIFT OFF!")
	else:
		print(num)
		time.sleep(0.1)
		countdown(int(num)-1)

def search(str, letter):
	for n in str:
		if n == letter:
			return True
	return False

def index(str, letter):
	i = 0 
	while i < len(str):
		if str[i] == letter:
			return i 
		i += 1
	return index(str,letter,-1)

def fibonacci(n):
	a = [0,1,1,2,3,5,8,13,21,34]
	return a[n]