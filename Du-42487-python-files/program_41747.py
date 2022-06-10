n = int(input())

i = 0
while i <= 100:
   if n % 5 == 0 and n % 3 == 0:
      print("fizz-buzz")
   elif n % 3 == 0:
   	print("fizz")
   elif n % 5 == 0:
   	print("buzz")
   else:
   	print(n) 
   	i = i + 1 


