import time

def countdown(num):
	while num >= 1:
		print(num)
		time.sleep(.1)
		num = num - 1
	if num == 0:
		print("LIFT OFF!")

