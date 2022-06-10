import time
def countdown(number):
	while number >=1:
		time.sleep(0.1)
		print(number)
		num = num -1
		if num == 0:
			time.sleep(0.1)
			print("LIFT OFF")