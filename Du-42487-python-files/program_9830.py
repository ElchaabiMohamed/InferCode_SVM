import time 
def countdown(m):
	while m > 0: 
		print(m)
		m = m - 1
		time.sleep(0.1)
		if m == 0:
			print("LIFT OFF!")

def search(string,letter):
	if letter not in string:
		return "False"
	else:
		return "True"
