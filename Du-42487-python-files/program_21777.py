def countdown(num):
	import time

	while num >= 1:
		print(num)
		time.sleep(0.1)
		num = num - 1

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
	print('calling search function')
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
	'calling index function.'
	print(index('python', 'i'))
	print(index('python','o'))

def fibonacci(n):
	Fval = 0
	Sval = 1
	i = 0
	while i <= n:
		if n <= 1:
			return n
		else:
			Next = Fval + Sval
			Fval = Sval
			Sval = Next
		i = i + 1
	return Next

if __name__ == '__main__':
	print('calling fibonacci function')
	print(fibonacci(0))
	print(fibonacci(6))
