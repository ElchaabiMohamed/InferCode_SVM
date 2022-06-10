n = 1
while n < 101:
	if n % 5 == 0 and n % 3 == 0:
		print("fizzbuzz")
	elif n % 3 == 0:
		print("fizz")
	elif n % 5 == 0:
		print("buzz")
	else:
		print(n) 
	n = n + 1 
   	


