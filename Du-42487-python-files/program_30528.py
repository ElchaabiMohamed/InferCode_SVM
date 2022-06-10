def countdown(n):
	import time

	if n ==1:
		print(n)
		time.sleep(0.1)
		print('LIFT OFF!')
	else:	
		print(n)
		time.sleep(0.1)
		countdown(n - 1)