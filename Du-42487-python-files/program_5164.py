import time,sys

def countdown(num):
	if num == 0:
		print("LIFT OFF!")
	else:
		print(num)
		num = num - 1
		time.sleep(0.1)
		return countdown(num)
