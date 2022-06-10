def countdown(num):
    while i > 0:
    	print (i)
    	i = i - 1
    if i == 0:
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
	if (n == 0):
		return 0
	elif (n == 1):
		return 1
	elif (n > 1):
		x = 0
		y = 1
		z = 2
		for i in range(3, n):
			x =  y + z
			y = z
			z = x
		return x
	else:
		retrun -1