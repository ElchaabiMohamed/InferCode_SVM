def countdown(num):
	while int(num) <= 1:
		print(num)
		time.sleep(0.1)
		num = int(num) - 1

	print("LIFT OFF!")

if __name__ == "__main__":
	countdown(3)