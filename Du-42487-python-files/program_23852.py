num = 0

while num < 101:
   if num % 5 == 0 and num % 3 == 0:
     print("Fizzbuzz")
   elif num % 3 == 0:
     print("Fizz")
   elif num % 5 == 0:
     print("Buzz")
   else:
     print(num)
   num = num + 1
