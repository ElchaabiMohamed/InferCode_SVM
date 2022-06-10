def countdown(num):
	num = eval(input())
	i = 0
	while i < len(num):
		cd = int(num)-i
		time.sleep(0.1)
		i = i + 1
