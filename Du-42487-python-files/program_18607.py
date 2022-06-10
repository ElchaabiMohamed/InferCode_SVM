def countdown(i):
	while i > 0:
		print (i)
		i = i - 1
	if i == 0:
		print("LIFT OFF!")
		countdown(i)