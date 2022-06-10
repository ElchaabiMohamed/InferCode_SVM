import time 

def countdown(num):
	i =0
	while i >= 1:
		print(num) 
		time.sleep(.1)
		num = num - 1
		i = i + 1
	print("LIFT OFF!")