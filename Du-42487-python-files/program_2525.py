import time

def countdown(num):
	if num == 0:
		print("LIFT OFF!")
	while num != 0:
		time.sleep(0.1)
		print(num)
		return countdown(num-1)

def search(str,letter):
	i = 0
	if len(str) == 0:
		return False
	elif str[0] == letter:
		return True
	else:
		return search(str[1:], letter)


def index(str,letter,num):
	i = 0
	while i < len(str):
		if str[i] == letter:
			return i
		else: 
			i = i + 1
	if i == len(str) :
		return '-1'


def fibonacci(n):
	list = [0]
	i = 0
	while n >= len(list):
		if len(list) > 1:
			new_num = list[i] + list[i-1] 
		else:
			new_num = list[i] + 1
		list.append(new_num)
		i = i + 1
	return list[-1]