a = 1
while a <= 100:
 
   if a%5 ==0 and a%3 ==0:
       print("fizzbuzz")

   elif a%3==0:
       print("fizz")

   elif a%5==0:
       print("buzz")
   else:
      print(a)

   a = a + 1