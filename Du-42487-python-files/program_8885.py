import time
def countdown(n):
 	while n > 0:
 		print(n)
 		n = n - 1
 		time.sleep(0.1)
 		if n == 0:
 			print("LIFT OFF!")

def search(string,letter):
	if letter not in string:
		return "False"
	else:
		return "True"



search("hello","a")
