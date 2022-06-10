def countdown(num):
	import time

	while num >= 1:
		print(num)
		time.sleep(0.1)
		num = int(num) - 1

	print("LIFT OFF!")

if __name__ == "__main__":
	print('Calling countdown function.')
	countdown(3)

def search(str,letter):
	if letter in str:
		print(True)
	else:
		print(False)

if __name__ == "__main__":
	print('calling search module')
	search('test', 'e')
	search('test', 'a')