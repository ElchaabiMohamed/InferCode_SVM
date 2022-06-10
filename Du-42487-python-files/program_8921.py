import time

def countdown(num):
	if num == 0:
		print("LIFT OFF!")
	else:
		print(num)
		time.sleep(0.1)
		countdown(num-1)
		
def search(str,letter):
	if str == "":
		return False
	elif str[0] == letter:
		return True
	else:
		search(str[1:], letter) 		#str[1:] not str-1
	
def index(str,letter,pos):		#confusing one!
	if pos == len(str):
		return -1
	elif str[pos] == letter:
		return pos
	else:
		index(str, letter, pos+1)
		
def fibonacci(n):
	if n == ((n-1) + (n-2)):
		return n
	else:
		fibonacci(n+1)
		















	