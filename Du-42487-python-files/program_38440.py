
n = 1
i = 0 

while n <= 100:
   if n % 3 == 0:
      print('fizz')
   elif n % 5 == 0:
      print('buzz')
   elif n % 5 == 0 and n % 3 == 0:
      print('fizzbuzz')
   else:
     print(n)
i = i + 1
