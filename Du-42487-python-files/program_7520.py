def countdown(num):
	import time
	i = 0
	while i < int(num):
		return int(num - i)
		time.sleep(0.1)
		i = i + 1

	print('LIFT OFF!')

def search(str,letter):
	if letter in str:
		return 'True'
	else:
		return 'False'
