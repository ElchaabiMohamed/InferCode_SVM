i = 1
while i < 101:
	if int(i) % 3 == 0 and int(i) % 5 != 0:
		print('fizz')
	elif int(i) % 5 == 0 and int(i) % 3 != 0:
		print('buzz')
	elif int(i) % 5 == 0 and int(i) % 3 == 0:
		print('fizzbuzz')
	else:
		print(i)
	i = i + 1
