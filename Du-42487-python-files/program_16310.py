#!usr/bin/env python

i = 1
while i <= 100:
   if i%3 == 0 and i%5 ==0:
      print("fizzbuzz")

   elif i%5 == 0:
      print("buzz")

   elif i%3 == 0:
      print("fizz")

   else:
      print(i)
   i = i + 1
