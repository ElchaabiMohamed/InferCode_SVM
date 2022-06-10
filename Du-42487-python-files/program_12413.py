import time

def countdown(num):
	i = 0
	while i < num:
		print(num)
		num = num - i
		time.sleep(0.1)
		print(num)
		i = i + 1

if __name__ == '__main__':
    print(countdown(3))