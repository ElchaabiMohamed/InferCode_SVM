def countdown(num):
	num=eval(input())
	i =0
	while i < num:
		print(num) 
		sleep(.1)
		num = num - 1
		i = i + 1
print("LIFT OFF!")