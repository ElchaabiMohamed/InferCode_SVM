def countdown(num):
	i = int(input())
	while i >=1:
		print(i)
		time.sleep(0.1)
		i = i - 1
	print("LIFT OFF!")