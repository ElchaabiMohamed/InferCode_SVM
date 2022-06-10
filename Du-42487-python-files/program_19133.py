import time

def countdown(num):
	while num >= 1 :
		print(num)
		time.sleep(0.1)
		num = num - 1
	print("LIFT OFF!")

if __name__ == '__main__':
    print(countdown(4))

