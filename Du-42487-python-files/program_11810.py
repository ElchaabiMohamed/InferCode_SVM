#countdown function
import time
def countdown(num):
	if num == 1:
		print(num)
		print("LIFT OFF!")
	else:
		print(num)
		time.sleep(0.1)
		countdown(num-1)

#search function
def search(str, letter):
	for item in str:
		if item == letter:
			return True
	return False

#index function
def index(str, letter,pos):
	if pos == len(str):
		return -1
	elif str[pos] == letter:
		return pos
	else:
		return index(str, letter, pos+1)

#fibonacci function
def fibonacci(n):
	a = [0,1,1,2,3,5,8,13,21,34]
	return a[n]