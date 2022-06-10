import time
def countdown(num):
	while num >=1:
		time.sleep(0.1)
		print(num)
		num = num -1
		if num == 0:
			time.sleep(0.1)
			print("LIFT OFF")