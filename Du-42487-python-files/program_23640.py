import time

def countdown(n):
	while n > 0:
		print(n)
		time.sleep(0.1)
		n = n - 1
	print("LIFT OFF!")
	
countdown(5)