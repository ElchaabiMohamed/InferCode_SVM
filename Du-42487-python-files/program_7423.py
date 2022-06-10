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