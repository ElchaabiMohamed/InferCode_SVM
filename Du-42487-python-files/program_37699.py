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
	i = 0
	while i < len(str):
		if str[i] == letter:
			return True
		i = i + 1
	return False


if __name__ == "__main__":
	print('calling search module')
	print(search('test', 'e'))
	print(search('test', 'a'))

def index(str,letter):
	i = 0
	while i < len(str):
		if str[i] == letter:
			return i
		i = i + 1
	return '-1'

if __name__ == '__main__':
	print(index('python', 'i'))
	print(index('python','o'))