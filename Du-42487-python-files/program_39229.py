#!/usr/bin/env python

n = 1

while n <= 10:
 if n % 3 == 0:
  print('Fizz')
 elif n % 5 == 0:
  print('Buzz')
 elif n % 3 == 0 and n % 5 == 0:
  print('FizzBuzz')  
n = n + 1
print(n)


 
