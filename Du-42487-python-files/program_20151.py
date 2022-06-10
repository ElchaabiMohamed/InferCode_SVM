
i=0
while i<100:
   n=i+1
   if n % 5 == 0 and n % 3 == 0:
      print("fizzbuzz")
   elif n % 5 == 0:
      print("buzz")
   elif n % 3 == 0:
      print("fizz")
   else:
      print(n)
   i=i+1
