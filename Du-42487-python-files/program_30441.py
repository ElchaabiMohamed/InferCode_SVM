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
	a = [0, 1]
	if len(a) == n+1:
		print(a[n])
	else:
		total = int(a[n]) + int(a[n+1])
		a.append(total)
		fibonacci(n+1)