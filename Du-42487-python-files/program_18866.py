import time
import sys

def countdown(num):
	while num >= 1:
		print(num) 
		time.sleep(0.1)
		num = num - 1
	print('LIFT OFF!')

if __name__ == '__main__':
	print('calling coundown(3)')
	print(countdown(5))

def search(word,letter):
	if letter in word:
		return True
	else:
		return False

if __name__ == '__main__':
	print(search('python','y'))

def index(word,letter):
	i = 0 
	while i < len(word):
		if letter not in word:
			return -1
		elif word[i] == letter:
			return i
		else:
			i = i + 1

if __name__ == '__main__':
	print(index('python','h'))

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		a = 0
		b = 1
		i = 2
		while i <= n:
			fib = a + b
			a = b
			b = fib
			i += 1
		return fib

if __name__ == '__main__':
	print(fibonacci(3))
		
