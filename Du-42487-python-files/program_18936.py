def countdown(num):
	import time
	num = eval(input())
	i = 0
	while i < int(num):
		cd = int(num)-i
		print(cd)
		time.sleep(0.1)
		i = i + 1
