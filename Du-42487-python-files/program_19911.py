import time

def countdown(num):
	i = 0
	while i < num:
		num = num - i
		print(num)
		time.sleep(0.1)
		i = i + 1



if __name__ == '__main__':
    print(countdown(3))

print("LIFT OFF!")