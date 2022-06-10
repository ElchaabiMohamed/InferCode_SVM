import time 
def countdown(num):
	i = 0
	while i < num:
		print(num - i)
		time.sleep(0.1)
		i = i + 1
	print("LIFT OFF!")

def search(str,letter):
	if letter in str:
		return "True"
	else:
		return "False"

def index(str,letter):
	i = 0
	while i < len(str):
		if letter in str[i]:
			return i
		i = i + 1
	else:
		return "-1"

def fibonacci(n):
	i = -1
	j = 1
	k = 1
	while i < n:
		j = k
		k = k + j
		i = i + 1
	return k





