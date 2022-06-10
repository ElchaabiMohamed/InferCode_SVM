def countdown(num):
	import time
	num = eval(input())
	i = 0
	while i < int(num):
		print(int(num - i))
		time.sleep(0.1)
		i = i + 1

	print('LIFT OFF!')
