def countdown(num):
	import time
	if num == 0:
		print('LIFT OFF!')
	else:
		print(num)
		countdown(num-1)

def search(str,letter):
	i = 0
	if letter == str[i]:
		return 'True'
	else:
		return 'False'

def fibonacci(n):
	#fibonacci list created to n+1 position
	i = 0
	a = [0, 1]
	if n == 0:
		return a[len(a)-1]
	else:
		total = int(a[i]) + int(a[i+1])
		a.append(total)
		i = i + 1
		fibonacci(n-1)

