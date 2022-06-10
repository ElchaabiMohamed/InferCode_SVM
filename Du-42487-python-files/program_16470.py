#countdown
def countdown(n):
	import time

	if n ==1:
		print(n)
		time.sleep(0.1)
		print('LIFT OFF!')
	else:	
		print(n)
		time.sleep(0.1)
		countdown(n - 1)


#search
def search(str, letter):
	if str == '':
		return False
	elif str[0] == letter:
		return True
	else:
		return search(str[1:], letter)

