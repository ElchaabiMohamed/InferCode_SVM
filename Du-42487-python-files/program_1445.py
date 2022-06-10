import time

def countdown(num):
	if num == 0:
		print('LIFT OFF!')
	else:
		print(num)
		time.sleep(0.1)
		countdown(num - 1)