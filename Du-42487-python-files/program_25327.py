import time

def countdown(num):
	if num == 0:
		print('LIFT OFF!')
	else:
		print(num)
		time.sleep(0.1)
		countdown(num - 1)

def search(ls,val):
	i = 0
	while i < len(ls):
		if ls[i] == val:
			return True
		i = i + 1
	return False

def index(str,letter):
	i = 0
	while i < len(str):
		if str[i] == letter:
			return i
		i = i + 1
	return '-1'
