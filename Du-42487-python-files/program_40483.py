import time

def countdown(num):
	while num >= 1 :
		print(num)
		time.sleep(0.1)
		num = num - 1
	print("LIFT OFF!")

if __name__ == '__main__':
    print(countdown(4))

def search(str,letter):
	if letter in str:
		return True
	else:
		return False

if __name__ == '__main__':
    print(search(abcd,a))

def index(str,letter):
	i = 0
	while i < len(str) and str[i] != letter:
		i = i + 1
	if i < len(str):
		return i
	else:
		return "-1" 

if __name__ == '__main__':
    print(index(abcd,a))