n = int(raw_input("number (1-100):"))

if n % 3 == 0 and n % 5 == 0:
   print "Fizz-Buzz"
else:
	if n % 3 == 0:
	   print "Fizz"
else:
	if n % 5 == 0:
	   print "Buzz"


