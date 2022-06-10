import time
def countdown(num):
	if num == 1:
		print(num)
		print("LIFT OFF!")
	else:
		print(num)
		time.sleep(0.1)
		countdown(num-1)

def search(str, letter):
	for n in str:
		if n == letter:
			return True
	return False

def index(str, letter):
	i = 0 
	while i < len(str):
		if str[i] == letter:
			return i 
		i += 1
	return