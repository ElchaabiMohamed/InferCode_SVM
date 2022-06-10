import time

def countdown(num):
	i = 0
	x = num
	while i < num:
		print(x)
		time.sleep(0.1)
		x = x - 1
		i = i + 1
	print("LIFT OFF!")

def search(str,letter):
	for item in str:
		if item == letter:
			return True
	return False
	

