import time

def countdown(n):
	while n > 0:
		print(n)
		time.sleep(0.1)	
		n = n - 1
		if n == 0:
			print("LIFT OFF!")
def search(string,letter):
	string = input()
	letter = input()
	if letter not in string:
		print("False")
	else:
		print("True")


