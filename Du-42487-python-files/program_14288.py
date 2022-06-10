import time

def countdown(num):
	while num != 0:
		time.sleep(0.1)
		return num
		num = num - 1
		i = i + 1
	if num == 0:
		return "LIFT OFF!"
