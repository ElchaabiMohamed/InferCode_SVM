i=1
while i<101:
   n=i
   if n % 3 == 0 and n % 5 == 0:
      n = "FizzBuzz"
   elif n % 5 ==0:
      n = "Buzz"
   elif n % 3==0:
      n = "Fizz"
   i+=1
   print(n) 
