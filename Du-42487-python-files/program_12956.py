num = 1

i = 0
while i < len(num):

   if num % 5 == 0 and num % 3 == 0:
      print("FizzBuzz")
   elif num % 5 == 0:
      print("Buzz")
   elif num % 3 == 0:
      print("Fizz")
   else:
      print(num)

num = num + 1

i = i + 1
  
   

