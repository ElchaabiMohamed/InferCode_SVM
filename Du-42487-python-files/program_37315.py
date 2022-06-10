import time 

def countdown(num):
	while num > 0:
		print(num) 
		num = num - 1
		time.sleep(0.1)
	return 'LIFT OFF!'

if __name__ == '__main__':
	print('calling coundown(3)')
	print(countdown(3))

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
	a = 0
	b = 1
	for i in range(0,n):
		print(a)

		temp = a
		a = b
		b = temp + b
	return a

if __name__ == '__main__':
	print(fibonacci(15))
		
