n = int(input())

if n % 3 == 0 and n % 5 == 0:
   print("Fizz-Buzz")
elif n % 3 == 0:
	print("Fizz")
else:
	if n % 5 == 0:
	   print("Buzz")


