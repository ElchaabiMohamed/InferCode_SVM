def countdown(num):
	import time
	i = 0
	while i < int(num):
		print(int(num - i))
		time.sleep(0.1)
		i = i + 1

	print('LIFT OFF!')

def search(str,letter):
	if letter in str:
		return 'True'
	else:
		return 'False'

def index(str,letter):
	i = 0
	while str[i] != letter:
		i = i + 1

	if i == len(str):
		return '-1'
	else:
		return i