n = int(input("number (1-100)"))


if n % 5 == 0 and n % 3 == 0:
   print("fizz-buzz")
elif n % 3 == 0:
	print("fizz")
elif n % 5 == 0:
	print("buzz")
else:
	print(n) 


