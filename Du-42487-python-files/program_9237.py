i = 0
while a < 100:
 
   if a%5 ==0 and a%3 ==0:
       print("Fizz-buzz")

   elif a%3==0:
       print("Fizz")

   elif a%5==0:
       print("Buzz")
   else:
      print(i)

a = a + 1
